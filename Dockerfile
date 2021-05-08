#Docker file contains all the commands to successfully deploy and run the service.
#It starts from fetching an image, moving code to a container, installing dependencies and starting the server.

From python:3.7-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt
# Not putting in requirements.txt as one can use requirements.txt for installing local dev dependencies
RUN pip install gunicorn

# gunicorn web server port
EXPOSE 5000

CMD ["sh", "gunicorn_web_server.sh"]
