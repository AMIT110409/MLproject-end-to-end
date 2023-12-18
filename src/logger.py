import logging # we import logging here because we want to use it in our logger class
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
 #here we are creating a log file with the name of current date and time
logs_path=os.path.join(os.getcwd(), "logs",LOG_FILE)  
#here we are creating a path for the log file
os.makedirs(logs_path,exist_ok=True) #here we are creating a folder with the name of logs and in that folder we are creating a file with the name of LOG_FILE

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #here we are creating a path for the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)s  - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# if __name__ == "__main__":
#     logging.info("This is a info message and logging has started")
    
    
