FROM node:latest

WORKDIR /home/app

COPY ./package.json ./
# COPY ./package-lock.json ./

RUN npm install

RUN npm install --save react react-dom react-scripts

COPY . .

# CMD ["npm", "start"]