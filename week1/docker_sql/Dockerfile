FROM python:3.9.10

RUN apt-get install wget

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app
RUN pip install -r requirements.txt

COPY sql_queries.py sql_queries.py
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]