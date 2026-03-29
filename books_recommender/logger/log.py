import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

# Create log dir if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Create filename based on timestamp
CURRENT_TIME_STAMP = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name = f"log_{CURRENT_TIME_STAMP}.log"
log_file_path = os.path.join(LOG_DIR, file_name)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    filemode='w',  # overwrite each run
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO  # NOTSET will log EVERYTHING, INFO is enough for normal logging
)

# ✅ Write something to the log
logging.info("Starting the books recommender system application.")