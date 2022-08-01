from flask_socketio import SocketIO
from website import app

socketio = SocketIO()

def create_socketio(app):
    """Creates socketio with eventlet async mode functionality.

    Args:
        app: The app to be configured.

    Returns:
        app: The configured app with socket async mode.
    """

    from . import events

    async_mode='eventlet'
    socketio.init_app(app, async_mode=async_mode)

    return app