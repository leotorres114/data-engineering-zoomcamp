#run postgres instance via docker, map PG_data to docker volume
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v db_volume:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13