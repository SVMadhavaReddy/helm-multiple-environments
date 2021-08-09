# Not optimized for production. Just an example Dockerfile!
FROM python:alpine3.14

WORKDIR /app

RUN pip install flask

# These are hardcoded for all the envs as this is just an example
ENV FLASK_APP=server
ENV FLASK_ENV=development

COPY server.py .

CMD [ "flask", "run" ]
