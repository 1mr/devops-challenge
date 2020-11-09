FROM node:10.23.0-alpine
WORKDIR  /usr/src/app

COPY package*.json /usr/src/app/
RUN yarn install
COPY . .
RUN yarn run build

ARG WEB_PORT=3001
ENV WEB_PORT=${WEB_PORT}

EXPOSE $WEB_PORT

USER node

CMD ["node", "dist/index.js"]
