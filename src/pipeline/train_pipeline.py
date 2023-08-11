import sys

from src.components.data_ingestion import DataIngestion
from src.exception import CustomException
from src.components.trainer import ModelTrainer




if __name__=='__main__':
    try:
        dat_ing=DataIngestion()
        train_data_path,test_data_path=dat_ing.data_ingestion()

        modeltrainer=ModelTrainer()
        model_name,mse,mae,r2_square=modeltrainer.initiate_model_trainer(train_data_path,test_data_path)
        print('model name: ',model_name)
        print('mse: ',mse)
        print('mae: ',mae)
        print('r2_square: ',r2_square)

    except Exception as e:
            raise CustomException(e,sys)