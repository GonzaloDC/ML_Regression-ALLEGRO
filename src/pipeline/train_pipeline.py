import sys

from src.components.data_ingestion import DataIngestion
from src.exception import CustomException
from src.components.trainer import ModelTrainer




if __name__=='__main__':
    try:
        dat_ing=DataIngestion()
        train_data_path,test_data_path=dat_ing.data_ingestion()

        # data_transformation=DataTransformation()
        # train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
        
        modeltrainer=ModelTrainer()
        print(modeltrainer.initiate_model_trainer(train_data_path,test_data_path))

    except Exception as e:
            raise CustomException(e,sys)