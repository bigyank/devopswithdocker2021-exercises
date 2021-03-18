➜ sudo docker build . -t docker-backend

➜ sudo docker build . -t docker-frontend

➜ sudo docker run -d -p 4000:8080 docker-backend

➜ sudo docker run -d -p 3000:5000 docker-frontend
