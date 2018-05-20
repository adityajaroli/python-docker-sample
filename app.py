from flask import Flask
from redis import Redis, RedisError
import os
import socket

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
	visits = redis.incr("counter")
    except RedisError:
	visits = "<i>Cannot connect</i>"

    html="<h3>Hello MR. {name}</h3> <br> <b>Visits:</b>{visits} <br> <b>Host:</b>{host}"

    return html.format(name=os.getenv("UserName", "SystemUser"), visits=visits, host=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


