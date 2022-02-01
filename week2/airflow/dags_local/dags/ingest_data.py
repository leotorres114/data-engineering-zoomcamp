import sys
import os
import psycopg2
import argparse
from sql_queries import *

def ingest_callable(user, password, host, port, db, table_name, csv_file, execution_date):
    db_params = {
    "dbname":f"{db}",
    "user":f"{user}",
    "password":f"{password}",
    "host":f"{host}",
    "port":f"{port}"
    }

    #connect to postgres server
    try:
        print("Connecting to PostgreSQL database")
        conn = psycopg2.connect(**db_params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")

    #initialize cursor
    cur = conn.cursor()

    #drop table if already exists
    cur.execute(drop_table(table_name))
    print("Table dropped successfully!")

    #create table
    cur.execute(create_table(table_name))
    print("Table created successfully!")

    #use copy_from to insert data to postres
    with open(csv_file, 'rt') as f:
        colnames = next(f)
        try:
            cur.copy_from(f, table_name, sep=",")
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error: {error}")
            conn.rollback()
            cur.close()
            return 1
        finally: 
            cur.close()
            conn.close()
            print("Postgres connection is now closed")

    return print(f"Data was successfully inserted into {table_name} table on {execution_date}")