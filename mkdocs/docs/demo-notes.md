# Demo Notes

## TODOs

- [ ] Figure out changelog handling
  - DEFERRED: do this incrementally as part of the walkthrough series
  - [ ] update changelog to reflect current project
  - [ ] automate changelog to apply updates with commits against main
- [ ] switch all hardcoded values to environment variables
- [ ] observability
  - [ ] adjust grafana dashboard to have useful display
  - [ ] setup observability w/ otel & grafana
    - api
    - postgres
    - https://github.com/Blueswen/fastapi-observability
    - https://github.com/grafana/loki/blob/main/production/docker/docker-compose.yaml
    - https://github.com/open-telemetry/opentelemetry-demo
  - [ ] otel collector: no way to have compose level health check (container has no shell)
  - [ ] redact sensitive data from signals - e.g. api headers w/ app tokens, etc.
- [ ] investigate: deprecated package for attributing functions with @deprecated
- [ ] documentation
  - [ ] treat log entries as means of internal documentation

## initial repo setup

- add readme.md based on template
- add changelog.md
- add .gitignore using `gi macos`
- git init
- uv venv
- uv pip install pre-commit
- add .pre-commit-config.yaml from template
- uv run pre-commit init
- git add all
- git commit
- (cycle through until all issues cleaned up)

## docker compose w/ postgres

- add docker-compose.yaml
- add .env
- [x] put .env in .gitignore and add .env.sample

## add api project

- uv init api
- update docker-compose
- add docker-compose.override.yml to support watch, etc.
- add prestart to run migrations
- add migration files / liquibase support files

## postgres + pydantic

- add ruff as dev dependency
- add basic route for /recipes and corresponding db retrieval logic
- add data seed migration script

## observability

### Metrics

* **TODO**

### Traces

* **TODO**

### Logs

- **loguru**
    - [loguru docs](https://loguru.readthedocs.io/en/stable/)
    - [loguru github](https://github.com/Delgan/loguru)

- **structlog**
    - [structlog docs](https://www.structlog.org/en/stable/)
    - [structlog github](https://github.com/hynek/structlog)

- [x] structured logging: loguru, python-json-logger, structlog

## documentation

- [x] use mkdocs + material for doc site

## technologies

- [ ] mkdocs [+ material]
- [ ] mkdocs + plantuml
- [ ] story mapping
- [ ] ADRs
- [ ] 12 factor app
- [ ] prometheus
- [ ] loki
- [ ] tempo
- [ ] grafana
- [ ] svg
- [ ] gRPC
- [ ] protobuf
- [ ] email catcher
- [ ] ASGI
- [ ] Starlette
- [ ] Postgres + Otel
- [ ] OpenAPI
- [ ] JSON Schema
- [ ] SQL Fluff
- [ ] Postman
- [ ] Curl
- [ ] Pytest
- [ ] Great Expectations
- [ ] Custom Client
  - Rich
  - Typer
- [ ] psycopg + otel
- [ ] jinja + otel?
- [ ] use a board (pivotal?); kanban vs. scrum
- [ ] JSON-LD
- [ ] DBML
  - https://dbml.dbdiagram.io/home
  - https://github.com/holistics/dbml
- [x] https://developers.google.com/search/docs/appearance/structured-data/recipe
open API spec -> Faker generated dataset
