import logging
from insurance.constant import *
import os

#from constant:
log_dir_path=LOG_DIR_PATH
log_file_path=LOG_FILE_PATH

#creating log dir:
os.makedirs(log_dir_path,exist_ok=True)

#logging:
logging.basicConfig(
    filename=log_file_path,
    filemode="w",
    format="[%(asctime)s]; %(name)s; %(levelname)s; %(message)s",
    level=logging.INFO
)