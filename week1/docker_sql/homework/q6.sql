WITH taxitrips AS
    (SELECT
    ytt.*,
    zpu."LocationID" AS puID,
    zpu."Zone" AS puZON,
    zdo."LocationID" AS doID,
    zdo."Zone" AS doZON
    FROM
    yellow_taxi_trips ytt
    LEFT JOIN zones zpu
        ON ytt."PULocationID" = zpu."LocationID"
    LEFT JOIN zones zdo 
        on ytt."DOLocationID" = zdo."LocationID"
    )
SELECT puID, puZON, doID, doZON, AVG(total_amount) AS "avg_fare"
FROM
  taxitrips
GROUP BY puID, puZON, doID, doZON
ORDER BY avg_fare DESC;