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


## PromQL

### Terminology

* **target**: object to scrape
    * e.g. _demo-api_
* **instance**: specific target endpoint to scrape
    * e.g. _demo-api @ 1.2.3.4:5678_ or _demo-api @ 1.2.3.4:5679_
* **job**: collection of instances
* **sample**: a single value at a point in time in a time series

### Data Types

* **instant vector**: a set of time series containing a single sample for each time series at a single shared/common point in time
* **range vector**: a set of time series containing a range of samples for each time series over a shared/common time period
* **scalar**: a single numeric (floating point) value
* **string**: a single string value

### Query Examples

The simplest query involves providing just a metric name (e.g. `http_requests_total`).  This will
return an instant vector containing elements for all time series that have this metric name.  The value
returned will be that of the most recent sample at or before the query's evaluation timestamp:

```
http_requests_total
```

The results can be filtered by providing a comma-separated list of label matchers in curly braces:

```
http_requests_total{job="lloyd-api",method="GET"}
```

Matching operators available:

* `=`: exactly equal
* `!=`: not equal
* `=~`: regex-match
    * `env=~"foo"` is equivalent to `env=~"^foo$"`
* `!~`: not regex-match

A range of samples (i.e. a range vector) can be retrieved by including a range vector selector in the query:

```
http_requests_total{job="lloyd-api"}[5m]
```

The value in square brackets is a float literal indicating how many seconds back in time the query should look in
retrieving samples.  The selector can also be represented using time units.  In the example above, the query
will return all samples recorded less than 5 minutes ago.  (The range is left-open, right-closed).

The `offset` modifier can be used to change the time offset for instant and range vectors in a query:

```
http_requests_total{job="lloyd-api"} offset 5m
```

The query above will return an instant vector containing the value of `http_request_total` 5 minutes in the past
relative to the query evaluation time.

The `@` modifier allows changing the evaluation time for instant and range vectors in a query.


```
http_requests_total{job="lloyd-api"} @ 1746075600
```

The query above will return an instant vector with sample values as of 2025-05-01 @ 00:00:00 CDT.

This can be combined with `offset`:

```
http_requests_total{job="lloyd-api"} offset 1h @ 1746075600

# OR

http_requests_total{job="lloyd-api"} @ 1746075600 offset 1h
```

Both queries above will return an instant vector with sample values as of 2025-04-30 @ 23:00:00 CDT.
