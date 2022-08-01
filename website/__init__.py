from flask import Flask
import os

from .restful import api

app = Flask(__name__)

UPLOAD_FOLDER = os.path.abspath("website\\uploads\\")


def create_api(app):
    """Creates REST API.

    Args:
        app: The app to which specified sources are added.
    """

    from .restful.resources import Face, FacesList, Image, ImagesList

    api.add_resource(Face, "/face/<string:filename>")
    api.add_resource(FacesList, "/faces")

    api.add_resource(Image, "/image/<filename>")
    api.add_resource(ImagesList, "/images")

    api.init_app(app)


app.config["SECRET_KEY"] = "437537haisf323764bncxm000"
directory = os.path.abspath("website\\uploads\\")

if directory[len(directory) - 1] != "/":
    directory += "/"

app.config["UPLOAD_FOLDER"] = directory
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

from website import routes
