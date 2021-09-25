FROM node:16-buster-slim

ENV HOST 0.0.0.0

COPY backend/docker/web/setup.sh /app/setup.sh

RUN chmod 755 /app/setup.sh

WORKDIR /app/src/

CMD [ "/app/setup.sh" ]
