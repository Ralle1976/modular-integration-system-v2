#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 YYYYMMDD"
  exit 1

BACKUP_DATE=$1

kubectl create job --from=cronjob/mysql-recovery mysql-recovery-$BACKUP_DATE \
  -n integration-system

kubectl wait --for=condition=complete job/mysql-recovery-$BACKUP_DATE \
  -n integration-system --timeout=300s