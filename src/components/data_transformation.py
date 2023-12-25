import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer  ## columns transformer is used to make pipeline for different columns
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from scipy import sparse  # Import the sparse module

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_obj
@dataclass   ## this class implements the dataclass decorator which is used to define class variable in it and can access it anywhere if we donot use it then we have to override the init method and then we can define class variable in it.
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts', "proprocessor.pkl") ## this line of code tells the path where we want to save the preprocessor object and the meaning of pickell file is that it is a binary file which is used to save the object in it.
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
            
    
    # def get_data_transformation_object(self):
        
    #     '''
    #         this function is responsible for getting the data transformation object
    #     '''
    #     try:
    #         numerical_columns = ["writing score","reading score"]
    #         categorical_columns = ["gender","race/ethnicity","parental level of education","lunch","test preparation course"]
            
    #         num_pipeline = Pipeline(
    #             steps=[
    #                 ("imputer", SimpleImputer(strategy="median")),
    #                 ("scaler", StandardScaler(with_mean=False) if sparse.issparse else StandardScaler()),  # Set with_mean=False for sparse matrices
    #         ]),
                
            
    #         cat_pipeline = Pipeline(
    #             steps=[
    #                 ("imputer", SimpleImputer(strategy="most_frequent")),
    #                 ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    
    #             ]
                    
    #         )
    #         logging.info("Numerical columns standard scaling completed")
    #         logging.info("Categorical columns encoding completed")
            
    #         preprocessor=ColumnTransformer(
    #             [
    #                 ("num_pipeline", num_pipeline, numerical_columns),
    #                 ("cat_pipeline", cat_pipeline, categorical_columns)
    #             ]
    #             #sparse_threshold=0.3  # Adjust the threshold as needed
    #         )
            
    #         return preprocessor
    #     except Exception as e:
    #         raise CustomException(e,sys) 
    
    def get_data_transformation_object(self):
        
        try:
            numerical_columns = ["writing score", "reading score"]
            categorical_columns = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]

            num_pipeline = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler(with_mean=False)),
            ]
            )
            cat_pipeline = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]
            )

            logging.info("Numerical columns standard scaling completed")
            logging.info("Categorical columns encoding completed")

            preprocessor = ColumnTransformer(
            transformers=[
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)


    def initiate_data_transformation(self,train_path,test_path):
        
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Read train and test data completed")
            
            logging.info("obtaining preprocessing object")
            
            preprocessing_obj =self.get_data_transformation_object()
            
            # target_column_name = "math score"
            
            target_column_name = "math score"

            # Convert column names to lowercase and remove leading/trailing spaces
            train_df.columns = [col.lower().strip() for col in train_df.columns]
            test_df.columns = [col.lower().strip() for col in test_df.columns]
                        
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feautre_train_df = train_df[target_column_name]
            numerical_columns = ["writing score", "reading score"]
                        
            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feautre_test_df = test_df[target_column_name]
            
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)  ## the differnce between fit_transform and transform
            ## is that fit_transform is used to fit the data and then transform it and transform is used to transform the data
            
            train_arr = np.c_[input_feature_train_arr,np.array(target_feautre_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feautre_test_df)]  ## here this line of code tells the numpy to concatenate the two arrays
            
            ## np.c_ means that it will concatenate the two arrays column wise
            
            logging.info(f"Saved preprocessing object.")
            
            save_obj(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
            