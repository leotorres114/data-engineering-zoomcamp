# Week 1 Review - Data Pipelines with Docker

## Docker
### What is a container? 
Isolated environment which can package applications, frameworks, and libraries in a standardized manner.

### Why should data engineers care about Docker?
- Reproducible (run pipeline locally or cloud)
- Experiment locally
- Integration tests (CI/CD)
- Can run multiple environments at the same time
- Lightweight and easy to maintain

### Hello World Docker Example

```bash
docker run hello-world
```

### Running a Postgres 13 Docker Image

```bash
docker run -it \
    -e POSTGRES_USER="user" \
    -e POSTGRES_PASSWORD="password" \
    -e POSTGRES_DB="database_name" \
    -v /volume/to/map:/var/lib/postgresql/data \
    -p containerport:hostport \
    postgres:13
```