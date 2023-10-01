#!/bin/bash

# Define the name of the Docker container
CONTAINER_NAME="dockerize_script"

# Check if the Docker container is already running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Container '$CONTAINER_NAME' is already running."
    echo "Attaching to container's stdout..."
    docker attach $CONTAINER_NAME
else
    # Check if the container exists (including stopped containers)
    if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
        # Start the existing container
        echo "Starting existing container: $CONTAINER_NAME..."
        docker start -i $CONTAINER_NAME
    else
        # Create and run a new container
        echo "Creating and running a new container: $CONTAINER_NAME..."
        docker build  -f ./Dockerfile --tag $CONTAINER_NAME .
        echo "==== Script output ====" 
        docker run --env-file .env --name $CONTAINER_NAME $CONTAINER_NAME
    fi
fi