FROM node:14-alpine AS development

ENV HOST 0.0.0.0

WORKDIR /app/src

# COPY ./src/package.json /app/src/

RUN apk update
# RUN apt-get update
# RUN apt-get update && \
# yarn install

COPY ./settings.json /app
COPY ./frontend/settingParser.js /app

COPY ./frontend/setup.sh /app/setup.sh
RUN chmod 755 /app/setup.sh

CMD [ "/app/setup.sh" ]
