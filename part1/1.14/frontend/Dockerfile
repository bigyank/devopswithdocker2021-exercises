FROM node
COPY . .
RUN npm install
RUN REACT_APP_BACKEND_URL=http://localhost:4000 npm run build 
RUN npm install -g serve
EXPOSE 5000
CMD [ "serve", "-s", "-l", "5000", "build" ]
