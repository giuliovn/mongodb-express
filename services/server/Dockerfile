FROM node:16.20-alpine3.18

WORKDIR /opt/server
COPY . .

RUN npm install 

EXPOSE 5050

ENTRYPOINT ["npm", "start"]
