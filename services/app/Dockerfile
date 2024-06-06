FROM node:16.20-alpine3.18

WORKDIR /opt/app
COPY . .

RUN npm install 

EXPOSE 3000

ENTRYPOINT ["npm", "start"]
