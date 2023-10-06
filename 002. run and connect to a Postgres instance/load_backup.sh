#!/bin/bash

# This script is used to load an existing .sql database backup file 
# to the database which is running inside the doker container.

#############################################
#        Things you should change
#############################################

CONTAINER_NAME="postgres-container"
DB_USERNAME="postgres"

#############################################
#        Rest of the script
#############################################

# Check if arguments were provided
if [ $# -eq 0 ]; then
  echo "No backup file name was provided"
  echo "Usage: $0 <database_name> <backup_file>"
  exit 1
fi

# Get the backup file name and DB name from the command-line argument
DB_NAME="$1"
BACKUP_FILE="$2"

# Step 1: Copy the .sql backup file into the container
docker cp "$BACKUP_FILE" "$CONTAINER_NAME":/db_backup/$BACKUP_FILE

# Step 2: Access the PostgreSQL container and restore the backup
docker exec -it "$CONTAINER_NAME" psql -U "$DB_USERNAME" -d "$DB_NAME" -a -f /db_backup/$BACKUP_FILE 

# Optional: Remove the backup file from the container (uncomment if needed)
# docker exec "$CONTAINER_NAME" rm /db_backup/backup.sql