# Deployment Guide

## System Requirements

- Docker 20.10+
- Kubernetes 1.22+
- Helm 3.0+ (optional)
- kubectl

## Quick Start

```bash
git clone https://github.com/Ralle1976/modular-integration-system-v2.git
cd modular-integration-system-v2
docker-compose up -d
```

## Environment Variables

Erforderliche Umgebungsvariablen in `.env`:

```env
MYSQL_HOST=localhost
MYSQL_USER=user
MYSQL_PASSWORD=password
GITHUB_TOKEN=your_token
GOOGLE_DRIVE_CREDENTIALS=your_credentials
OPENAI_API_KEY=your_key
```

## Security

- Alle Secrets in Kubernetes Secrets
- HTTPS erzwungen
- Network Policies implementiert
- Regular Security Audits