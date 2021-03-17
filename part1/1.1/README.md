docker run -d nginx x3
docker stop id1 id2
docker ps -a

## Output
➜ sudo docker ps -a      
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS     NAMES
5c707ed4b6ef   nginx     "/docker-entrypoint.…"   53 seconds ago   Exited (0) 14 seconds ago             suspicious_joliot
016b11585ce9   nginx     "/docker-entrypoint.…"   55 seconds ago   Exited (0) 14 seconds ago             beautiful_ishizaka
05f37555f330   nginx     "/docker-entrypoint.…"   58 seconds ago   Up 55 seconds               80/tcp    frosty_hoover
97170b317bea   nginx     "/docker-entrypoint.…"   30 minutes ago   Up 30 minutes               80/tcp    serene_khayya

