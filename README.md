# README

Build the Docker image from the root directory with:
```bash
docker build -t aws-bedrock-core-agent:0.1 -f docker/Dockerfile .
```

Test locally with:
```bash
source .venv/bin/activate && python agent-app.py
```
Alternatively, use docker-compose to build and run the application:
```bash
docker-compose -f ./docker/docker-compose.yml up --build
```