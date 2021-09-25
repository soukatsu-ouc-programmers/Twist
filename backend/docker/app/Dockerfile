FROM python:3.9.6

ENV PYTHONUNBUFFERD 1

RUN apt-get update

# COPY ../../src/app /app/src
COPY ./settings.json /app/settings.json

WORKDIR /app/src/

COPY ./backend/docker/app/setup.sh /app/setup.sh

RUN chmod 755 /app/setup.sh

CMD ["bash", "/app/setup.sh"]
