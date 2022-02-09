-- Question 1
SELECT EXTRACT(YEAR FROM pickup_datetime) as year, COUNT(1)
FROM `high-sunlight-339220.nyc_trips_all.fhv_tripdata_partitioned` 
GROUP BY year;

-- Question 2
SELECT EXTRACT(YEAR FROM pickup_datetime) as year, COUNT(DISTINCT(dispatching_base_num))
FROM `high-sunlight-339220.nyc_trips_all.fhv_tripdata_partitioned` 
GROUP BY year;

-- Question 3
-- Best strategy to optimize a queries that frequently filter by dropoff_datetime and order by dispatching_base_num? 
-- Option 3: Partition by dropoff_datetime and cluster by dispatching_base_num

-- Question 4
SELECT 
    COUNT(*)
FROM `high-sunlight-339220.nyc_trips_all.fhv_tripdata_partitioned` 
WHERE
    (dispatching_base_num = 'B00987' OR dispatching_base_num = 'B02060' OR dispatching_base_num = 'B02279')
    AND 
    (pickup_datetime >= '2019-01-01' AND pickup_datetime <= '2019-03-31');

-- Question 5
-- Best strategy when filtering on dispatching_base_num and SR_Flag? 
-- Option 3: Cluster by dispatching_base_num and SR_Flag

-- Question 6
-- What improvements can be seen by partitioning/clustering for data size less than 1 GB? 
-- Option 2: Worse performance due to metadata