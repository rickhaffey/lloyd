# Demo Notes

## initial repo setup

add readme.md based on template
add changelog.md
[ ] update changelog to reflect current project
[ ] automate changelog to apply updates with commits against main
add .gitignore using `gi macos`
git init
uv venv
uv pip install pre-commit
add .pre-commit-config.yaml from template
uv run pre-commit init
git add all
git commit
(cycle through until all issues cleaned up)

## docker compose w/ postgres
add docker-compose.yaml
add .env
[ ] put .env in .gitignore and add .env.sample

## add api project
uv init api
update docker-compose
add docker-compose.override.yml to support watch, etc.
add prestart to run migrations
add migration files / liquibase support files


## postgres + pydantic

add ruff as dev dependency
add basic route for /recipes and corresponding db retrieval logic
add data seed migration script

## observability

[ ] setup observability w/ otel & grafana
    - api
    - postgres
    - https://github.com/Blueswen/fastapi-observability
    - https://github.com/grafana/loki/blob/main/production/docker/docker-compose.yaml
    - https://github.com/open-telemetry/opentelemetry-demo
[ ] structured logging: loguru, python-json-logger, structlog
[ ] redact sensitive data from signals - e.g. api headers w/ app tokens, etc.



[ ] deprecated package for attributing functions with @deprecated


## documentation

[ ] treat log entries as means of internal documentation
[ ] use mkdocs + material for doc site
