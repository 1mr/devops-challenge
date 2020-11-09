FROM node:10.23.0-alpine
WORKDIR  /usr/src/app
COPY package*.json /usr/src/app/
RUN yarn install
COPY . .
RUN yarn run build

ARG NODE_ENV=development
ENV NODE_ENV=${NODE_ENV}
ARG WEB_PORT=3002
ENV WEB_PORT=${WEB_PORT}

EXPOSE $WEB_PORT

USER node

CMD ["node", "dist/index.js"]