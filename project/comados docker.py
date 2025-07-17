docker-compose down --volumes --remove-orphans
docker system prune --all --volumes –force

docker-compose build --no-cache

docker-compose up


docker-compose down
docker-compose up --build
