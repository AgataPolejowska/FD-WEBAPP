from website import app
from werkzeug.debug import DebuggedApplication
from website.socketio import create_socketio, socketio
from website import create_api


create_api(app)
create_socketio(app)


if __name__ == '__main__':
    app.debug = True
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    socketio.run(app)