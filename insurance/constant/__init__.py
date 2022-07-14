import os
from datetime import datetime

#root Dir , Project Dir & current time stamp 
ROOT_DIR=os.getcwd()
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%y-%m-%d_%H-%M-%S')}"

#logger constant
LOG_DIR="log"
LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"
LOG_DIR_PATH=os.path.join(ROOT_DIR,LOG_DIR)
LOG_FILE_PATH=os.path.join(LOG_DIR_PATH,LOG_FILE_NAME)