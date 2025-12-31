import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m-%d_%Y_%H-%M-%S')}.log"

log_path = os.path.join("logs")

#os.makedirs(os.path.dirname(log_path), exist_ok=True)

os.makedirs(log_path, exist_ok=True)  # Create the logs directory itself

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO,
        filename=LOG_FILEPATH,
        format='[%(asctime)s] %(lineno)d %(name)s %(levelname)s]- %(message)s'   
)