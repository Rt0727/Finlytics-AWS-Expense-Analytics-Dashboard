#!/bin/bash

# Define backup location and date format
BACKUP_DIR="./backups"
DATE=$(date +\%Y-\%m-\%d_\%H-\%M-\%S)
BACKUP_FILE="$BACKUP_DIR/db-backup-$DATE.sql"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Perform backup using pg_dump
PGPASSWORD=$DB_PASSWORD pg_dump -h $DB_HOST -U $DB_USERNAME $DB_NAME > $BACKUP_FILE

echo "Backup completed: $BACKUP_FILE"