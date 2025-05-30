.DEFAULT_GOAL := help


startup: ## Run all platform services (postgres, otel-collector, grafana, etc.) and application services (api, etc.) locally via docker compose
	docker compose -f docker-compose.yml -f docker-compose.override.yml up --build --watch

shutdown: ## Shutdown all platform and application services running locally via docker compose
	docker compose -f docker-compose.yml -f docker-compose.override.yml down --volumes

startup-api: ## Run just the API and its dependencies (postgres, pre-start, etc.)
	docker compose -f docker-compose.yml -f docker-compose.override.yml up --build --watch api


startup-otel-collector: ## Run just the API and its dependencies (postgres, pre-start, etc.)
	docker compose -f docker-compose.yml -f docker-compose.override.yml up --build --watch otel-collector

startup-docs: ## Run just the mkDocs dev server
	docker compose -f docker-compose.yml -f docker-compose.override.yml up --build --watch mkdocs

precommit: ## Run all pre-commit checks and fixes against all files
	uv run pre-commit run --all-files

# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
