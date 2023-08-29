import os
import sys
import logging

message = "[%(asctime)s, %(levelname)s, %(module)s, %(message)s]"
logging_dir = "logs"
log_filePath = os.path.join(logging_dir, "running_logs.logs")
os.makedirs(logging_dir, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = message,

    handlers=[
        logging.FileHandler(log_filePath), # show logs in file
        logging.StreamHandler(sys.stdout)  # show logs in terminal
    ]
)

logger = logging.getLogger("loggerLibrary")