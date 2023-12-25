import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation   ## this line we write because we want to use the class DataTransformation which is present in the file data_transformation.py and we want to use it in this file so we need to import it here
from src.components.data_transformation import DataTransformationConfig

@dataclass ### it is a decorater which takes a class and adds some functionality to it and with the help of this we can define class variable in it and can access it anywhere if we donot use it then we have to override the init method and then we can define class variable in it.
class DataIngestionConfig: 
    train_data_path = os.path.join('artifcats',"train.csv") # path to train data
    test_data_path = os.path.join('artifcats',"test.csv") 
    raw_data_path = os.path.join('artifcats',"data.csv") 
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(r"D:\Downloads\Stud.csv")
            # df=pd.read_csv('notebook\data\stud.csv')  ## here we are reading the data from the csv file and storing it in the variable df
            logging.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  # this line will create a folder with the name of artifcats and in that folder it will create a file with the name of train.csv
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) # this line will create a folder with the name of artifcats and in that folder it will create a file with the name of data.csv
            
            logging.info("train test split initiated")
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42) ## this line will split the data into train and test set
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) 
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True) 
            
            logging.info("Ingestion  of the data iss completed successfully")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                
            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == '__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()   ## here we are calling the function initiate_data_ingestion() which is present in the class DataIngestion and we are storing the return value of this function in the variable train_data and test_data

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # modeltrainer=ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
       
    
