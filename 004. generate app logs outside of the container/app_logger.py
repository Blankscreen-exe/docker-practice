# file acts as a helper function repositry within your application.
# you can use this logger to send logs to stdout, logs.txt file or even in a database

import time
import os

def app_logger(log_message: str) -> None:
    """
    Used to log messages send by the application
    These messages will be sent to the stdout and written in the logs.txt file
    """
    
    # get the log file path
    log_file = os.environ.get("LOG_FILE_PATH", "logs.txt")
    
    # Get the current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # check if it is DEBUG environment or not
    if bool(os.environ.get("DEBUG", 1)):
        
        # Print the log message with timestamp
        with open(log_file, "a") as log_file:
            print(f"[{timestamp}] - {log_message}", file=log_file)
            
        # or log the message in stdout
        print(f"[{timestamp}] - {log_message}")
    