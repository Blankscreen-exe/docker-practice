FROM python:3

# Copy your application code
COPY generate_logs.py /app/generate_logs.py

# Copy the logging configuration into the container
COPY ./logging_config.json /etc/docker/daemon.json

WORKDIR /app

CMD ["python", "generate_logs.py"]