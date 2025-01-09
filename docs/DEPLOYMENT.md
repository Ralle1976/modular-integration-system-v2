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

## Detailed Deployment Options

### Local Development
```bash
docker-compose up -d
docker-compose logs -f
```

### Production Deployment

1. Kubernetes Config anwenden:
```bash
kubectl apply -f kubernetes/
```

2. Status überprüfen:
```bash
kubectl get pods -l app=modular-system
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

## Monitoring & Logging

- Prometheus Metrics endpoint: `/metrics`
- Grafana Dashboard verfügbar
- Log Aggregation via ELK Stack

## Backup & Recovery

Siehe [BACKUP.md](./BACKUP.md) für Details.

## Security Considerations

- Alle Secrets in Kubernetes Secrets gespeichert
- HTTPS erzwungen
- Network Policies implementiert
- Regular Security Audits

## Scaling

- Horizontal Pod Autoscaling konfiguriert
- Ressourcenlimits gesetzt
- Load Balancing aktiviert

## Troubleshooting

Siehe [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

## Support

Bei Fragen oder Problemen:
1. Issue auf GitHub erstellen
2. Wiki konsultieren
3. Maintainer kontaktieren