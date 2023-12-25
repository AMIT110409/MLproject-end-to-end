import sys 
sys.path.append(r'D:\MLproject-end-to-end')  # Add the project root to sys.path
from src.logger import logging

#sys module  provide access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

## 2222 line ka point hai ye import logging # we import logging here because we want to use it in our logger class

  ## it is not working this line so we need to check why logss file are not created for exception.py 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #exc_info() method returns a tuple of three values that give information about the exception that is currently being handled.
    file_name=exc_tb.tb_frame.f_code.co_filename #co_filename is the filename from which the code was compiled
    error_message="Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message    

    #Python: Activated environment for .\mlvenv\python.exe


class CustomException(Exception):   ##here we are making a class CustomException which is inheriting the Exception class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)   ##super is used for inheritance here we are inheriting the Exception class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
        
if __name__ == '__main__':
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)
           
        
        
    