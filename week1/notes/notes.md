# Week 1 Review

# Data Pipelines with Docker
## Docker
### What is a container? 
Isolated environment which can package applications, frameworks, and libraries in a standardized manner.

### Why should data engineers care about Docker?
- Reproducible (run pipeline locally or cloud)
- Experiment locally
- Integration tests (CI/CD)
- Can run multiple environments at the same time
- Lightweight and easy to maintain

# SQL Refresher
## Joins
### Join using WHERE
```sql
SELECT 
	tpep_pickup_datetime,
	tpep_dropoff_datetime, 
	total_amount,
	CONCAT(zpu."Borough",'/',zpu."Zone") AS "pickup_loc",
	CONCAT(zdo."Borough",'/',zdo."Zone") AS "dropoff_loc",
FROM 
	yellow_taxi_trips t,
	zones zpu,
	zones zdo
WHERE
	t."PULocationID" = zpu."LocationID" AND
	t."DULocationID" = zdo."LocationID"
```

### OR you can use JOIN statements instead of WHERE
```sql
SELECT 
	tpep_pickup_datetime,
	tpep_dropoff_datetime, 
	total_amount,
	CONCAT(zpu."Borough",'/',zpu."Zone") AS "pickup_loc",
	CONCAT(zdo."Borough",'/',zdo."Zone") AS "dropoff_loc",
FROM 
	yellow_taxi_trips t JOIN zones zpu
	ON t."PULocationID" = zpu."LocationID"
	JOIN zones zdo
	ON t."DULocationID" = zdo."LocationID"
```

### Aggregations 
```sql
SELECT 
	CAST(tpep_dropoff_datetime AS DATE) as "day",
	"DOLocationID",
	COUNT(1),
	MAX(total_amount),
	AVG(passenger_count)
FROM 
	yellow_taxi_data t
GROUP BY
	CAST(tpep_dropoff_datetime AS DATE) OR 
	1, 2 /* you can group by integers too
ORDER BY "day" ASC;
```

# Terraform and GCP
1. What is Terraform?
	- open-source tool by Hashicorp, used for provisioning infrastructure resources
	- supports DevOps best practices for change management
	- Managing configuration files in source control to maintain an ideal state for testing and production env
2. What is IaC?
	- Infrastructure-as-Code
	- build, change, and manage your infrastructure in a safe, consistent, and repeatable way by defining resource configurations that you can version, reuse, and share
3. Some advantages
	- Infrastructure lifecycle management
	- Version control commits
	- Very useful for stack-based deployments, and with cloud providers such as AWS, GCP, Azure
	- State-based approach to track resource changes throughout deployments

## Google Cloud Platform
- Service Account - a pipeline, web service, etc. Basically an account for services. Restricted/limited permissions. 
- Data Lake - a bucket where we store raw data in organized fashioned. compressed with certain file types (parquet, csv, etc.)
- BigQuery - data warehouse to store more structured data
