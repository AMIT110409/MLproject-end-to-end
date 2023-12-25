## here i am writing common code which can be used in other files also for this i am making a file utils.py and writing the code in it

import os
import sys
import dill ## this is used for saving the object

import numpy as np
import pandas as pd

from sklearn.metrics import r2_score

from src.exception import CustomException

from sklearn.model_selection import GridSearchCV

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
    
# def evaluate_models(X_train, y_train,X_test,y_test,models,param):
#     try:
#         report = {}
        
#         # for model_name, model in models.items():
#         #     try:
#         #         para = param[model_name]
#         #     except KeyError:
#         #         para = {}  # Default to an empty dictionary if parameters are not provided
#         for model_name, model in models.items():
#             para = param.get(model_name, {})  # Use get() to provide a default empty dictionary if key not found


#         for i in range(len(list(models))):
#             model = list(models.values())[i]
#             para=param[list(models.keys())[i]]
#             gs = GridSearchCV(model,para,cv=3)
#             gs.fit(X_train,y_train)

#             model.set_params(**gs.best_params_)
#             model.fit(X_train,y_train)

#             #model.fit(X_train, y_train)  # Train model

#             y_train_pred = model.predict(X_train)

#             y_test_pred = model.predict(X_test)

#             train_model_score = r2_score(y_train, y_train_pred)

#             test_model_score = r2_score(y_test, y_test_pred)

#             report[list(models.keys())[i]] = test_model_score

#         return report

#     except Exception as e:
#         raise CustomException(e, sys)    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for model_name, model in models.items():
            try:
                para = param.get(model_name, {})  # Use get() to provide a default empty dictionary if key not found

                gs = GridSearchCV(model, para, cv=3)
                gs.fit(X_train, y_train)

                model.set_params(**gs.best_params_)
                model.fit(X_train, y_train)

                # Evaluate the model on the test set
                y_test_pred = model.predict(X_test)
                test_model_score = r2_score(y_test, y_test_pred)

                report[model_name] = test_model_score
            except Exception as e:
                raise CustomException(e, sys)
    except Exception as e:
        raise CustomException(e, sys)

    return report
