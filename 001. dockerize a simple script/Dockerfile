# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt (if any)
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Load existing environment variables
COPY .env .env
# Define environment variable
ENV TEXT_TO_PRINT "Hello World"

# Load environment variables from the .env file
RUN export $(cat .env | xargs)

# Run script.py when the container launches
CMD ["python3", "main.py"]