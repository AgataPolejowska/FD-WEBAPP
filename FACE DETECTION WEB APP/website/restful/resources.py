import os
from flask import request
from flask.json import jsonify

from restful import Resource, abort
from flask_restful import Api

from website.utils import allowed_file, get_faces

from . import api

api = Api()

UPLOAD_FOLDER = os.path.abspath('website\\uploads\\')
IMAGES = {}
FACES = {}


def abort_if_file_exists(filename):
    """Checks if uploaded file already exists.

    Args:
        filename (str): The name of the file.
    """
    if filename in IMAGES:
        abort(404, message="File {} exists".format(filename))


class Image(Resource):
    """Represents the uploaded file as a resource.
    """
    def post(self):
        """POST method used for uploading a new file by the client.
        """
        file = request.files['file']
        new_filename = file.filename
        path = os.path.join('UPLOAD_FOLDER', new_filename)
        file.save(path)

    def delete(self, filename):
        """Delete the specified image.
        """
        for key, value in dict(IMAGES).items():
            print(key, value, filename)
            if value['image filename'] == str(filename):
                print("deleting", filename, IMAGES)
                del IMAGES[key]
                print(IMAGES)

class ImagesList(Resource):
    """Represents the list of uploaded files by the client as a resource.
    """
    def get(self):
        """GET method used for sending JSON to the client with uploaded images list.
        """
        return jsonify(uploads=IMAGES)

    def post(self):
        """POST method used for uploading a new file by the client.
        """
        file = request.files['file']
        if allowed_file(file.filename):
            abort_if_file_exists(file.filename)
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            file = {'image filename' : file.filename}
            IMAGES[len(IMAGES)+1] = file
        else:
            abort(422)


class Face(Resource):
    """Represents the face resource that is detected in the uploaded image.
    """
    def get(self, filename):
        """GET method for sending the JSON with detected faces information for appropriate display.

        Args:
            filename (str): The name of the file.

        Returns:
            JSON with detected faces list (appropriate coordinates indicating the position of the faces on the image).
        """
        path = os.path.join(UPLOAD_FOLDER, filename)
        detected_faces = get_faces(path)
        faces = []
        for detected_face in detected_faces:
            print('detected_face', detected_face)
            x, y, width, height = detected_face['box']
            faces.append({'face' : {
                "xMin" : x,
                "yMin" : y,
                "xMax" : x + width,
                "yMax" : y + height
                }
            })
        FACES[filename] = faces
        return jsonify(faces=FACES)


class FacesList(Resource):
    """Represents the detected faces list.
    """
    def get(self):
        return FACES
