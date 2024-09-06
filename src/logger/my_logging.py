import os
from datetime import datetime
import logging

# Set up log file
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")

# Create log directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create file handler
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter(
    "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Optional: Also log to console
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)


def get_logger():
    """
    Returns the logger instance configured with the logging settings.
    """
    return logger
