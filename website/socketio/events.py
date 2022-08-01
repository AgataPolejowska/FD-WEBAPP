from flask_socketio import emit   

from . import socketio

clients = 0

@socketio.on("connect", namespace="/")
def connect():
    """Registers a new client connection.
    """
    global clients
    clients += 1
    emit("users", {"user_count": clients}, broadcast=True)

@socketio.on("disconnect", namespace="/")
def disconnect():
    """Registers the disconnected client.
    """
    global clients
    clients -= 1
    emit("users", {"user_count": clients}, broadcast=True)


    