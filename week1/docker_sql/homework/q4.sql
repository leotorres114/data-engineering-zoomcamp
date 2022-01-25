SELECT
	CAST(tpep_pickup_datetime AS DATE) as "day",
	MAX(tip_amount) as "tip"
FROM yellow_taxi_data
GROUP BY
	"day"
ORDER BY tip desc
LIMIT 10;