# DevOps Essentials Assignment

This project is a basic Python Flask web app that tracks visit counts using a Redis backend. It demonstrates core DevOps practices: containerization, orchestration, CI/CD, and health monitoring.

## Features

- Flask application with routes:
  - `/`: Welcome page
  - `/visit`: Visit counter stored in Redis
  - `/health`: Returns Redis connection status
- Dockerized with a lightweight Python base image
- Managed via Docker Compose with persistent Redis storage
- Health check endpoint for use in CI and orchestration
- CI pipeline via GitHub Actions that tests app health

## How to Build and Run Locally

Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/), then run:

```bash
docker-compose up --build