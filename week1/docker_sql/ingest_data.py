import sys
import os
import psycopg2
import argparse
from sql_queries import *

def connect(params):
    db_params = {
    "dbname":params.db,
    "user":params.user,
    "password":params.password,
    "host":params.host,
    "port":params.port
    }

    conn = None
    try:
        #connect to postgres server
        print("Connecting to PostgreSQL database")
        conn = psycopg2.connect(**db_params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn

def insert_data(conn, cur, params):
    table = params.table_name
    url = params.url
    csv_name = 'output.csv'

    os.system(f'wget {url} -O {csv_name}')
    
    with open(csv_name, 'rt') as f:
        colnames = next(f)
        try:
            cur.copy_from(f, table, sep=",")
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error: {error}")
            conn.rollback()
            cur.close()
            return 1
    print(f"Data was successfully inserted into {table} table")
    cur.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    #set up connection and cursor
    conn = connect(args)
    cur = conn.cursor()

    #execute drop and create table queries before inserting data
    cur.execute(drop_table(args))
    print("Table dropped successfully!")
    cur.execute(create_table(args))
    print("Table created successfully!")

    #insert taxi data to table
    insert_data(conn, cur, args)