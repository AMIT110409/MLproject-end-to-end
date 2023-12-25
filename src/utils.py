## here i am writing common code which can be used in other files also for this i am making a file utils.py and writing the code in it

import os
import sys
import dill ## this is used for saving the object

import numpy as np
import pandas as pd

from src.exception import CustomException

def save_obj(file_path, obj):
    '''
        this function is responsible for saving the object
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)          ## dill is called as a pickle on steroids for python object serialization and deserialization 
    except Exception as e:
        raise CustomException(e, sys)