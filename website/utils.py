import matplotlib.pyplot as plt
import mtcnn


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	"""Checks if the file has allowed extension.

	Args:
		filename (str): The name of the file uploaded.

	Returns:
		bool: True if the file is supported, false otherwise.
	"""
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_faces(img_path):
	"""Gets the lits of faces detected by MTCNN detector.

	Args:
		img_path (str): The path to the image.

	Returns:
		list: The list of faces bounding box coordinates.
	"""
	img = plt.imread(img_path)
	detector = mtcnn.MTCNN()
	faces = detector.detect_faces(img)
	return faces
	