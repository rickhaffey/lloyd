# Observability


## Dashboard Queries


### FastAPI Observability

#### Total Requests

`sum(fastapi_requests_total{app_name="$app_name", path!="/metrics"})`

Query options:

- interval: 1m
- relative time: 24h

Transformations:

- Series to Rows
- Sort By: time

#### Requests Count

`fastapi_requests_total{app_name="$app_name", path!="/metrics"}`

Query options:

- interval: 1m
- relative time: 24h

- legend: {{method}} {{path}}

Transformations:

- Series to Rows
- Sort By: time
- Partition by Values:
