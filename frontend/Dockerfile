FROM node:22-alpine

WORKDIR /app

COPY . /app

RUN npm install @vue/cli@5.0.8 -g
RUN npm i

# пока без билда
CMD [ "npm", "run", "serve" ]