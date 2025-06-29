#how to write logs to a file and change the log level
import logging  # Import logging module

# Set logging to write logs to a file named 'app.log', with level INFO and specific format
logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.INFO,  # Log only INFO and above (no DEBUG)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format includes timestamp, level, and message
)

logging.debug("This will not be logged")  # DEBUG is lower than INFO, so it won't appear
logging.info("App started")               # INFO message will be logged
logging.warning("Low disk space")         # WARNING message will be logged
