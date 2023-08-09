FROM node:12-alpine
WORKDIR /app
COPY entrypoint.sh /app/
COPY package*.json ./
RUN npm i
COPY index.js index.js
CMD ["sh", "entrypoint.sh"]
