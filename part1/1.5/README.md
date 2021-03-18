➜ sudo docker pull devopsdockeruh/simple-web-service:alpine
➜ sudo docker images

|REPOSITORY   |TAG    |IMAGE ID   |CREATED   |SIZE   |
|---|---|---|---|---|
|devopsdockeruh/simple-web-service   |ubuntu   |4e3362e907d5   |3 days ago   |83MB   |
|devopsdockeruh/simple-web-service   |alpine   |fd312adc88e0   |3 days ago   |15.7MB   |


➜ sudo docker run -d --name alpine devopsdockeruh/simple-web-service:alpine
➜ sudo docker exec -it alpine sh
