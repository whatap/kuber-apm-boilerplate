FROM node:12-alpine
WORKDIR /app
COPY whatap.conf /app/
COPY package*.json ./
RUN npm i
COPY index.js index.js
CMD ["npm", "start"]
