#!/bin/bash

#############################################
#        Things you should change
#############################################

# Check if arguments were provided
if [ $# -eq 0 ]; then
  echo "No backup file name was provided"
  echo "Usage: $0 <database_name>"
  exit 1
fi

# set the name of the database you want the backup of
DB_NAME="$1"

#############################################
#        Things you should NOT change
#############################################

# Set the current date and time as a backup identifier
backup_id=$(date +'%Y-%m-%d_%H:%M')
# set the name of the output file
OUTPUT_FILE="db_backup_${DB_NAME}_${backup_id}.sql"

#############################################
#        Rest of the script
#############################################

# Run the PostgreSQL container if it's not already running
if ! docker ps -q -f name=postgres-container &>/dev/null; then
    echo -e "\033[1;34mStarting PostgreSQL container...\033[0m"
    docker run --name postgres-container -e POSTGRES_PASSWORD=yourpassword -d -p 5432:5432 -v pg_backup:/backup postgres
else
    echo -e "\033[1;34mPostgreSQL container is already running...\033[0m"
fi

# Dump the PostgreSQL database to a file inside the container
docker exec postgres-container mkdir /db_backup
docker exec -it --privileged --workdir /db_backup postgres-container pg_dump -U postgres -w -F p -d $DB_NAME > $OUTPUT_FILE

# Copy the backup file from the container to a folder on your host system
if [ ! -f "$OUTPUT_FILE" ]; then
    docker cp postgres-container:/db_backup/$OUTPUT_FILE "/workspaces/docker-practice/002. run and connect to a Postgres instance"
fi

# success/failure message
if [ -f "/workspaces/docker-practice/002. run and connect to a Postgres instance/$OUTPUT_FILE" ]; then
    echo -e "\033[0;32m$OUTPUT_FILE was copied to:"
    pwd
    echo -e "\033[0m"
else
    echo -e "\033[0;31m$OUTPUT_FILE was not found\033[0m"
fi

