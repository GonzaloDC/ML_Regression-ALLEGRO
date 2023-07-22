from src.exception import CustomException
import sys
import os

import pandas as pd
import numpy as np 
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV



def load_data(path):

    df_name='clean_dataset_completo.csv'
    df_path:str=os.path.join(path,df_name)
    
    
    df=pd.read_csv(df_path)

    return df


def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try: 
        report={}
        for i in range(len(models)):
            model = list(models.values())[i]
            para=params[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report


    except Exception as e:
        raise CustomException(e,sys)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)



# if __name__=="__main__":
#     try:
#         path = str=os.path.join('artifacts','data_clean')
#         print(path)
#         df=load_data(path)
#         # df = merge_data(path)
#         print(df.head(2))
#     except Exception as e:
#         raise CustomException(e,sys)