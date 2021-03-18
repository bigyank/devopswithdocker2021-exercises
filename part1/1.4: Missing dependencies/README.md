sudo docker run -it ubuntu apt-get update; apt-get install curl -y; sh -c 'echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website;'


