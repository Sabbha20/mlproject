import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d%m%Y_%H%M%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs",datetime.now().strftime('%d-%b-%Y'))
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] | %(name)s - %(lineno)d | [%(levelname)s]: %(message)s",
)

# if __name__ == "__main__":
#     logging.info("Starting the script")