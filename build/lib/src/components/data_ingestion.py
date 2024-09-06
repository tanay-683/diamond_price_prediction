import pandas as pd
import numpy as np
from src.logger.my_logging import my_logging
from src.exception.exception import customException

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


class DataIngestionConfig:
    # these are the configuration of current component
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        my_logging.info("Data Ingestion Started")
        try:
            data = pd.read_csv('/home/tanay/mlops/train.csv') 
            my_logging.info("Readign a DataFrame")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            # storing the "data" in the directory made just above
            # data.to_csv(path)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)

            my_logging.info("Performing train_test_split")
            train_data, test_data = train_test_split(data, test_size=0.25)
            my_logging.info("Data splitting completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            my_logging.info("Data Ingestion Completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            my_logging.info()
            raise customException(e,sys)
    


if __name__=='__main__':
    obj=DataIngestion()