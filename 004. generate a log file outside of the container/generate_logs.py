# This module is used for generating dummy logs along with timestamps
# These logs are generated to the stdout

import time
import random

# dummy log messages
log_messages = [
    "Application started",
    "Processing request...",
    "Warning: Disk space is low",
    "Error: Connection timeout",
    "Database updated successfully",
]

def generate_dummy_logs():
    """throws log messages to stdout infinitly along with timestamps
    """
    while True:
        # Choose a random log message
        log_message = random.choice(log_messages)
        
        # Get the current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Print the log message with timestamp
        with open("logs.txt", "a") as log_file:
            print(f"[{timestamp}] - {log_message}", file=log_file)
            
        print(f"[{timestamp}] - {log_message}")
        
        # Sleep for a random interval (simulating log generation)
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    generate_dummy_logs()
