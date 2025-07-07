#format the logs
import logging  # Import the logging module

# Set logging with a custom format: LEVEL:LOGGER_NAME:MESSAGE
logging.basicConfig(
    format='%(levelname)s:%(name)s:%(message)s',  # Custom format
    level=logging.INFO  # Minimum level to display is INFO
)

# Log an INFO message using the defined format
logging.info("Formatted info message")
