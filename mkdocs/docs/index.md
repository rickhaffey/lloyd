
# LLoyd

The Bartender

![Lloyd the Bartender](images/lloyd-the-bartender.png)

## Links

### API

* [Swagger](http://localhost:8000/docs)
* [ReDoc](http://localhost:8000/redoc)
* [Recipes](http://localhost:8000/recipes)

### Adminer

* [Adminer](http://localhost:8080/?pgsql=postgres&username=postgres&db=lloyd&ns=public)

### Prometheus

* [Prometheus](http://localhost:9090)

### Loki

* [Labels API](http://localhost:3100/loki/api/v1/labels)
* [Loki API Docs](https://grafana.com/docs/loki/latest/reference/loki-http-api/)


### Tempo

* [Tags API](http://localhost:3200/api/search/tags)
* [Tempo API Docs](https://grafana.com/docs/tempo/latest/api_docs/)

### Grafana

* [Grafana](http://localhost:3000/?orgId=1&from=now-6h&to=now&timezone=browser)
* [Dashboard](http://localhost:3000/d/fastapi-observability/fastapi-observability?orgId=1&from=now-5m&to=now&timezone=browser&var-app_name=&var-log_keyword=&refresh=5s)


### OpenTelemetry

* [opentelemetry-collector (Github)](https://github.com/open-telemetry/opentelemetry-collector)
* [opentelemetry-collector-contrib (Github)](https://github.com/open-telemetry/opentelemetry-collector-contrib)


### Docker

* [Docker CLI Reference](https://docs.docker.com/reference/cli/docker/)
* [Docker Compose Reference](https://docs.docker.com/compose/)
* [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/)
* [Docker Compose File Reference](https://docs.docker.com/reference/compose-file/)

## MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

### Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

### Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
