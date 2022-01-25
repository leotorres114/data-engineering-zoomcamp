SELECT 
	CAST(tpep_pickup_datetime AS DATE) as "day",
	COUNT(1)
FROM yellow_taxi_data 
WHERE
	CAST(tpep_pickup_datetime AS DATE) = '2021-01-15'
GROUP BY
	CAST(tpep_pickup_datetime AS DATE);