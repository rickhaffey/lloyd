# Demo Notes

## initial repo setup

- add readme.md based on template
- add changelog.md
- [ ] update changelog to reflect current project
- [ ] automate changelog to apply updates with commits against main
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
- [ ] put .env in .gitignore and add .env.sample

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

- [ ] setup observability w/ otel & grafana
    - api
    - postgres
    - https://github.com/Blueswen/fastapi-observability
    - https://github.com/grafana/loki/blob/main/production/docker/docker-compose.yaml
    - https://github.com/open-telemetry/opentelemetry-demo
- [ ] structured logging: loguru, python-json-logger, structlog
- [ ] redact sensitive data from signals - e.g. api headers w/ app tokens, etc.


- [ ] deprecated package for attributing functions with @deprecated
- [ ] switch all hardcoded values to environment variables

- [ ] otel collector: no way to have compose level health check (container has no shell)

## documentation

- [ ] treat log entries as means of internal documentation
- [x] use mkdocs + material for doc site


## preliminary schema

**recipes**
id: int, auto-increment
name: string(255), not null, unique
description: string(?) null

**recipe_instructions**
id:
recipe_id: FK
text: string(255)
sort_oder: int

**ingredients**
id
name

**recipe_ingredients**
recipe_id: FK
ingredient_id: FK
quantity: float
units:
sort_index: int



## technologies

- [ ] prometheus
- [ ] loki
- [ ] tempo
- [ ] grafana
- [ ] svg
- [ ] mkdocs [+ material]
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
- [ ] story mapping
- [ ] 12 factor app
- [ ] mkdocs + plantuml
- [ ] JSON-LD
- [ ] DBML
  - https://dbml.dbdiagram.io/home
  - https://github.com/holistics/dbml
- [ ] https://developers.google.com/search/docs/appearance/structured-data/recipe
open API spec -> Faker generated dataset
