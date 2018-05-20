#Docker file contains all the commands to successfully deploy and run the service.
#It starts from fetching an image, moving code to a container, installing dependencies and starting the server.

From python:2.7-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80


CMD ["python", "app.py"]
