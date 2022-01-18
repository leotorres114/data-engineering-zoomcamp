import sys
import psycopg2
from sql_queries import create_table

def connect(db_param):
    conn = None
    try:
        #connect to postgres server
        print("Connecting to PostgreSQL database")
        conn = psycopg2.connect(**db_param)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn

def insert_data(conn, cur, filepath:str, table:str):
    with open(filepath, 'rt') as f:
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
    db_param = {
    "dbname":"ny_taxi",
    "user":"root",
    "password":"root",
    "host":"localhost",
    "port":"5432"
    }

    #set up connection and cursor
    conn = connect(db_param)
    cur = conn.cursor()

    #execute create table query
    cur.execute(create_table)
    print("Table created successfully!")

    #insert taxi data to table
    insert_data(conn, cur, "taxidata.csv", "yellow_taxi_data")