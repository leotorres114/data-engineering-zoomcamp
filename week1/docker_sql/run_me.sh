!#/bin/bash

#build dockerized .py script from Dockerfile
docker build -t taxi_ingest:v001 .

#create docker network to connect dockerized script to postgres database
docker network create pg-network

#create docker volume to map database to
docker volume create db_volume

#run postgres docker container
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v db_volume:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:13

#run dockerized ingest_data.py script, connect to postgres database via docker network
docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url="https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv"
