from flask import render_template, send_file
from website import app



@app.route('/', methods=['GET', 'POST'])
def index():
    """The route for the main page.

    Returns:
        Renders designed template for main page.
    """
    return render_template('index.html')


@app.route('/image/<f>', methods=['GET'])
def upload(f):
    """The route for handling uploaded image and sending to the client.

    Args:
        f (str):The image path.

    Returns:
        Sends the file as a response.
    """
    uploads = app.config['UPLOAD_FOLDER']
    return send_file(uploads + f)