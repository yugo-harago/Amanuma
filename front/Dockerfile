
FROM node:16

RUN mkdir /app
WORKDIR /app

COPY package*.json ./
RUN npm ci

# COPY package.json pnpm-lock.yaml .npmrc ./
# RUN pnpm install --frozen-lockfile

COPY . .

RUN npm run build

EXPOSE 8080
CMD ["npm", "run", "serve"]
