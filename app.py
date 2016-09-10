import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

app = Flask(__name__)
sio = socketio.Server()

@app.route("/")
def  index():
		return render_template('index.html')

@sio.on("connect", namespace="/chat")
def connect(sid, env):
	print("connect ", sid)
	sio.emit("connect", "you're connected", room = sid)


if __name__ == '__main__':

	app = socketio.Middleware(sio, app)

	eventlet.wsgi.server(eventlet.listen(("", 5000)), app)