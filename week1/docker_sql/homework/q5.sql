SELECT
    CAST(tpep_pickup_datetime AS DATE) as "day",
    "PULocationID",
    COUNT(1) AS "trips",
FROM yellow_taxi_data
WHERE
    CAST(tpep_pickup_datetime AS DATE) = '2021-01-14'
GROUP BY
    "day"
ORDER BY trips DESC;