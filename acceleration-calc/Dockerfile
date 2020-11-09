FROM node:10.23.0-alpine as builder
WORKDIR  /usr/src/app
COPY package*.json /usr/src/app/
RUN yarn install
COPY . .
RUN yarn run build


FROM node:10.23.0-alpine
WORKDIR  /usr/src/app
COPY --from=builder /usr/src/app/dist dist
COPY . .

ARG NODE_ENV=development
ENV NODE_ENV=${NODE_ENV}
ARG WEB_PORT=3000
ENV WEB_PORT=${WEB_PORT}
ARG DV_URL=http://127.0.0.1:3001/dv
ENV DV_URL=${DV_URL}
ARG A_URL=http://127.0.0.1:3002/a
ENV A_URL=${A_URL}

RUN if [ "$NODE_ENV" = "production" ] ; then yarn install --production=true ; else yarn install ; fi

EXPOSE $WEB_PORT

USER node

CMD ["node", "dist/index.js"]
