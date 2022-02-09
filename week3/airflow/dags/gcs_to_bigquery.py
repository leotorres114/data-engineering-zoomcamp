import os
import logging
from datetime import date

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", "nyc_trips_all")

INPUT_PATH = "raw"
FILETYPE = "PARQUET"
DATA_COLUMN = {"yellow": "tpep_pickup_datetime", "fhv": "pickup_datetime"}#, "green": "lpep_pickup_datetime"}

default_args = {
    "owner": "airflow",
    "start_date": days_ago(0),
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="gcs_to_bigquery_dag",
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['dtc-de'],
) as dag:

    for data, column in DATA_COLUMN.items():
        move_files_task = GCSToGCSOperator(
            task_id=f"move_{data}_tripdata_files_task",
            source_bucket=BUCKET,
            source_object=f"{INPUT_PATH}/{data}_*.{FILETYPE}",
            destination_bucket=BUCKET,
            destination_object=f"{data}/",
            move_object=True
        )

        gcs_to_bigquery_external_task = BigQueryCreateExternalTableOperator(
            task_id=f"bigquery_external_{data}_tripdata_table_task",
            table_resource={
                "tableReference": {
                    "projectId": PROJECT_ID,
                    "datasetId": BIGQUERY_DATASET,
                    "tableId": f"external_{data}_tripdata",
                },
                "externalDataConfiguration": {
                    "sourceFormat": FILETYPE,
                    "sourceUris": [f"gs://{BUCKET}/{data}/*"],
                },
            },
        )

        CREATE_PART_TBL_QUERY = f"""CREATE OR REPLACE TABLE {BIGQUERY_DATASET}.{data}_tripdata_partitioned \
                                PARTITION BY DATE({column}) \
                                AS \
                                SELECT * FROM {BIGQUERY_DATASET}.external_{data}_tripdata;"""

        bigquery_external_to_partition_task = BigQueryInsertJobOperator(
            task_id=f"bigquery_{data}_tripdata_external_to_partition_task",
            configuration={
                "query": {
                    "query": CREATE_PART_TBL_QUERY,
                    "useLegacySql": False,
                }
            }
        )

        move_files_task >> gcs_to_bigquery_external_task >> bigquery_external_to_partition_task