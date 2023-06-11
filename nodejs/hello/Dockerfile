FROM node:12-alpine
EXPOSE 80
RUN mkdir -p /app
WORKDIR /app
COPY whatap.conf /app/
COPY package*.json /app/
RUN npm i
COPY index.js /app/
CMD ["npm", "start"]
