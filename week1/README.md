# Week 1 Review - Data Pipelines with Docker

## Overview
In Week 1 of DataTalks.Club's [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp), we were introduced to creating containerized data pipelines using Docker. 

Here's an overview of the (fairly straightforward) workflow:

![data pipepine](img/wflow.jpg)

The lesson uses [Yellow Taxi Trip Records](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) data collected Jan-2021 from NYC's Taxi and Limousine Commission (TLC). The data is downloaded, processed, and inserted into a Postgres database via the `ingest_data.py` script running on a Python Docker container built from the repo's Dockerfile. This container talks to the Postgres database (running on a separate container) via a Docker network. Once the data is in Postgres, we can run analytical queries via pgcli. To access the database via pgcli, run the following command in Terminal. 

```shell
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

As an example query, to get the total number of records in the data, we can run:

```SQL
SELECT COUNT(1) FROM YELLOW_TAXI_DATA;
```
which will output: 

| count   |
|---------|
| 1369765 |

## Deviations from DE Zoomcamp
While this data pipeline follows the same workflow as the DE Zoomcamp, I challenged myself to use as much vanilla Python as possible (for the sake of learning Python). So, besides the standard libraries, I only used the [psycopg2](https://www.psycopg.org) library (a Postgres adapter for Python) whereas the DE Zoomcamp used Pandas for data processing and SQL Alchemy for connecting to the database. 

## Run the Pipeline
To actually run the pipeline (on MacOS or Linux), simply run the `run_me.sh` bash script: 
```bash
bash run_me.sh
```
The script builds the Python Docker image from the repo's Dockerfile, creates a Docker network and Docker volume to map the database to (for persistent data storage) and runs both the Postgres and Python Docker containers. Note: *this bash script assumes that Docker is already running!*
