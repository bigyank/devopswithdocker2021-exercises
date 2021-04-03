
#!/bin/sh
if [ -z "$1" ]; then
  echo "Please set github repo"
  exit
fi

if [ -z "$2" ]; then
  echo "please set container name"
  exit
fi


if [ -z "$3" ]; then
  echo "please set dockerhub username"
  exit
fi

if [ -z "$4" ]; then
  echo "please set dockerhub password"
  exit
fi

git clone $1 repo
cd repo

if [ ! -f "Dockerfile" ]; then
  echo "Dockerfile is not present"
  exit
fi

docker build -t $2 .


docker login -u $3 -p $4
docker push $2
