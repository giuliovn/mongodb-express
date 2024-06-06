FROM node:16.20-alpine3.18

# ENV NODE_OPTIONS="--openssl-legacy-provider"
COPY . .

RUN npm install 

EXPOSE 3000

ENTRYPOINT ["npm", "start"]
