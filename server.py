from flask import Flask
from redis import Redis, RedisError
import os
import socket
import logging


class AppServer:
    def __init__(self, host='0.0.0.0', port=8082):
        self.host = host
        self.port = port
        # self.redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
        self.logger = logging.getLogger()
        self.ENV = os.environ.get('APP_ENV', 'Dev')

    def create_server(self):
        self.logger.info(f'Starting Flask App')
        app = Flask(__name__)
        self.__register_routes(app)
        return app

    @staticmethod
    def __register_routes(app):
        @app.route("/hello")
        def hello():
            try:
                # visits = self.redis.incr("counter")
                visits = 1
            except RedisError:
                visits = "<i>Cannot connect. Please check if redis service is running or not</i>"
            html = "<h3>Hello MR. {name}</h3> <br> <b>Visits:</b>{visits} <br> <b>Host:</b>{host}"
            return html.format(name=os.getenv("UserName", "SystemUser"), visits=visits, host=socket.gethostname())


if __name__ == "__main__":
    app_server = AppServer()
    app = app_server.create_server()
    debug_app = True if app_server.ENV.lower() == "dev" else False
    app.run(host='0.0.0.0', port=8080, debug=debug_app)

