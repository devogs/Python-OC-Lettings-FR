#!/bin/bash
# run_local_docker.sh: Single command to run the final Docker image locally,
# securely loading environment variables from the local .env file.

# --- Configuration ---
# NOTE: Replace YOUR_DOCKER_USERNAME with your actual Docker Hub username
IMAGE_NAME="YOUR_DOCKER_USERNAME/oc-lettings-site"
TAG="latest" 

echo "--- Pulling and Running Docker Image: ${IMAGE_NAME}:${TAG} ---"

# --- Load Environment Variables ---
# The 'set -a' command exports all subsequent variables, making them available 
# to 'docker run' when passed with the -e flag.
set -a
# Source the .env file to load the SECRET_KEY, SENTRY_DSN, etc.
if [ -f .env ]; then
    source .env
    echo ".env file loaded successfully."
else
    echo "ERROR: .env file not found! Cannot run securely."
    exit 1
fi
set +a # Stop exporting variables

# 1. Pull the image from Docker Hub
docker pull "${IMAGE_NAME}:${TAG}"

# 2. Run the container, passing only the necessary variables from the shell environment
# NOTE: DJANGO_DEBUG=False is explicitly set here as it's mandatory for production mode.
docker run -d --rm \
    --name oc-lettings-site-local \
    -p 8000:8000 \
    -e SECRET_KEY="${SECRET_KEY}" \
    -e SENTRY_DSN="${SENTRY_DSN}" \
    -e SENTRY_LOG_LEVEL="${SENTRY_LOG_LEVEL}" \
    -e SENTRY_EVENT_LEVEL="${SENTRY_EVENT_LEVEL}" \
    -e DJANGO_DEBUG="False" \
    -e ALLOWED_HOSTS="*" \
    # Using the local SQLite database is fine for local testing via Docker
    -e DATABASE_URL="sqlite:///db.sqlite3" \
    "${IMAGE_NAME}:${TAG}"

echo "--- Site should be accessible at http://localhost:8000 ---"
echo "Container ID: $(docker ps -q -f name=oc-lettings-site-local)"