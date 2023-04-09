# /office/Dockerfile
FROM node:16

RUN mkdir /app
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

RUN npm run build

EXPOSE 8081
CMD ["npm", "run", "serve"]
