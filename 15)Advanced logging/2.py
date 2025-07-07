#custom logger
# utils/custom_logger.py

import logging  # Import logging module

# Function to create and return a custom logger
def custom_logger(log_level=logging.DEBUG):
    logger = logging.getLogger(__name__)  # Create logger with current module's name
    logger.setLevel(log_level)            # Set the log level

    # Create a file handler to log messages to 'selenium.log'
    file_handler = logging.FileHandler("selenium.log")

    # Define the format of the log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)  # Set the format for the file handler

    # Avoid adding multiple handlers if already exists
    if not logger.hasHandlers():
        logger.addHandler(file_handler)

    return logger  # Return the configured logger

# Usage example
logger = custom_logger()  # Create custom logger instance
logger.info("Launching browser")  # Log an info message
