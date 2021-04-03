FROM node:alpine as build-stage
WORKDIR /frontend
COPY . .
RUN npm install -only=production && \ 
    npm run build 

FROM nginx:alpine
COPY --from=build-stage /frontend/build /usr/share/nginx/html
