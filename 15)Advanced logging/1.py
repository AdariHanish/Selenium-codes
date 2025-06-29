#advanced logging
import logging  # Import logging module

# Create a logger object with name "MyLogger"
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)  # Set logger to capture all levels from DEBUG and above

# Create a file handler to write WARNING and above logs to a file
file_handler = logging.FileHandler("advanced.log")
file_handler.setLevel(logging.WARNING)  # Only WARNING and above will go to the file

# Create a console handler to show logs in the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Show all levels in console

# Create a log formatter with timestamp, level and message
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Attach the formatter to both handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Attach handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example log messages
logger.debug("Debug log")  # Will appear in console only
logger.warning("This warning will go to both console and file")  # Goes to both