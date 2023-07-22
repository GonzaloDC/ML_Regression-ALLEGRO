import os
import sys 

from dataclasses import dataclass
from src.exception import CustomException
from src.utils import load_data

from sklearn.model_selection import train_test_split




@dataclass
class IngestionConfig:
    data_path: str=os.path.join('artifacts','data_clean')
    train_data_path: str=os.path.join('artifacts','data_clean','train.csv')
    test_data_path: str=os.path.join('artifacts','data_clean','test.csv')
    
    

class DataIngestion:
    def __init__(self):
        self.ingestion_conf=IngestionConfig()

    def data_ingestion(self):
        try:
            df = load_data(self.ingestion_conf.data_path)
            os.makedirs(os.path.dirname(self.ingestion_conf.train_data_path),exist_ok=True)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_conf.train_data_path,index=False)
            test_set.to_csv(self.ingestion_conf.test_data_path,index=False)

            return (self.ingestion_conf.train_data_path,
                    self.ingestion_conf.test_data_path)

        except Exception as e:
            raise CustomException(e,sys)    
        

# if __name__=="__main__":
#     try:
#         data_ing=DataIngestion()
#         train_path,test,path=data_ing.data_ingestion()

#         # data_transformation=DataTransformation()
#         # train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

#     except Exception as e:
#         raise CustomException(e,sys)