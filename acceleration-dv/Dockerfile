FROM node:10.23.0-alpine
WORKDIR  /usr/src/app

RUN apk add --no-cache tini=0.18.0-r0
ENTRYPOINT ["/sbin/tini", "-e", "131", "-e", "143", "--"]

COPY package*.json /usr/src/app/
RUN yarn install
COPY . .
RUN yarn run build

ARG WEB_PORT=3001
ENV WEB_PORT=${WEB_PORT}

EXPOSE $WEB_PORT

USER node

CMD ["node", "dist/index.js"]
