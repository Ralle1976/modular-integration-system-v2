# Deployment Guide

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t modular-system .
```

2. Run with docker-compose:
```bash
docker-compose up -d
```

## Kubernetes Deployment

1. Apply the manifests:
```bash
kubectl apply -f kubernetes/
```

## CI/CD Pipeline

The system uses GitHub Actions for automated testing, building and deployment.

### Pipeline Stages

1. Test: Runs the test suite
2. Build: Builds and pushes the Docker image
3. Deploy: Deploys to Kubernetes