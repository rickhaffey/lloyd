# 2. Use Loguru for logging

Date: 2025-05-30

## Status

Accepted

## Context

We need to be able to easily log details about system activity and behavior.  Additionally, having the logs in a
structured format will improve our ability to locate and interpret the generated logs.

## Decision

We will use [Loguru](https://loguru.readthedocs.io/en/stable/) as our main tool for logging as it simplifies the
code required for logging configuration (as compared against the standard python logging libraries), and provides
good support out of the box for supporting structured logging.

## Consequences

Logging setup becomes as simple as

```python
from loguru import logger
logger.info("that's all there is to it")
```

Structured logging requires one additional step. (The example below will log to the console, but alternative
[sinks](https://loguru.readthedocs.io/en/stable/api/logger.html#sink) are relatively easy to set up):

```python
logger.add(sys.stdout, serialize=True)
```

One risk we'll need to consider is how the format of the structured logging produced (in JSON format) aligns
with the requirements of whatever log aggregation and analytic tooling we decide to use.
