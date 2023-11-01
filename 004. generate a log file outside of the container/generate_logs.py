# This module is used for generating dummy logs along with timestamps
# These logs are generated to the logs.txt

import random
import time
from app_logger import app_logger

# dummy log messages
log_messages = [
    "Application started",
    "Processing request...",
    "Warning: Disk space is low",
    "Error: Connection timeout",
    "Database updated successfully",
]

def generate_dummy_logs():
    """throws log messages to stdout and logs.txt infinitly along with timestamps
    """
    while True:
        # Choose a random log message
        log_message = random.choice(log_messages)
        
        # call the app logger to log messages
        app_logger(log_message)
        
        # Sleep for a random interval (simulating log generation)
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    generate_dummy_logs()
