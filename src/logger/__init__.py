import os
import sys
import logging

from datetime import datetime

##creating a log directory for logging the timestamp
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

###current timestamp using f-string
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

###file name would be nothing but the current timestamp and .log&log_ in the end as well as in the beginning respectively
file_name = f"log_{CURRENT_TIME_STAMP}.log"

#joining the log directory and the file name
logging_file_path = os.path.join(LOG_DIR, file_name)

##final logging configuration
logging.basicConfig(

                    filename = logging_file_path,
                    filemode = "w",
                    format ='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO 

                    )