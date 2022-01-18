#create yellow taxi data postgres table

create_table = """CREATE TABLE IF NOT EXISTS yellow_taxi_data (
        VendorID VARCHAR, 
        tpep_pickup_datetime TIMESTAMP WITHOUT TIME ZONE, 
        tpep_dropoff_datetime TIMESTAMP WITHOUT TIME ZONE, 
        passenger_count VARCHAR, 
        trip_distance FLOAT(53), 
        RatecodeID VARCHAR, 
        store_and_fwd_flag TEXT, 
        PULocationID BIGINT, 
        DOLocationID BIGINT, 
        payment_type VARCHAR, 
        fare_amount FLOAT(53), 
        extra FLOAT(53), 
        mta_tax FLOAT(53), 
        tip_amount FLOAT(53), 
        tolls_amount FLOAT(53), 
        improvement_surcharge FLOAT(53), 
        total_amount FLOAT(53), 
        congestion_surcharge FLOAT(53)
)
"""