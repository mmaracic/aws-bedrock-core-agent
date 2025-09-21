# Minimal Dockerfile using official Python 3.12 slim image
FROM python:3.12-slim

# Do not run as root
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Install minimal build deps if needed and cleanup to keep image small
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirement file if present to leverage Docker cache
COPY requirements.txt ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy project files (user can override in docker-compose for dev)
COPY *.py /app

USER appuser

# Default command: show python version (quick smoke). Override to run your app.
CMD ["python", "--version"]
