import os
from datetime import datetime
import logging

# log file ka naam datetime ke hisaab se banaya h, kyoki naya naam kaha se layenge aur datetime se hume kuch info bhi mil jayegi
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.log"

log_path = os.path.join(os.getcwd(), "logs") # this will create a folder named "logs" in the current working directory# tb_frame is an attribute of traceback object which returns the frame object or file of the traceback object


os.mkdir(log_path) if not os.path.exists(log_path) else None

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")


# if __name__ == "__main__":
#     logging.info("This is an info message")