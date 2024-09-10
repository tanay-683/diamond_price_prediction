import pandas as pd
import numpy as np
from src.logger.my_logging import get_logger
from src.exception.exception import customException

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


# Initialize the logger
logger = get_logger()


class DataIngestionConfig:
    # these are the configuration of current component
    raw_data_path: str = os.path.join("artifact", "raw.csv")
    train_data_path: str = os.path.join("artifact", "train.csv")
    test_data_path: str = os.path.join("artifact", "test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info("Data Ingestion Started")
        logger.info("Data Ingestion Started")
        try:
            data = pd.read_csv("/home/tanay/mlops/train.csv")
            logger.info("Reading a DataFrame")  # Update logger statement
            os.makedirs(
                os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),
                exist_ok=True,
            )
            data.to_csv(self.ingestion_config.raw_data_path, index=False)

            logger.info("Performing train_test_split")  # Update logger statement
            train_data, test_data = train_test_split(data, test_size=0.25)
            logger.info("Data splitting completed")  # Update logger statement

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logger.info("Data Ingestion Completed")  # Update logger statement

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            logger.error(e)  # Update logger statement
            raise customException(e, sys)


# if __name__=='__main__':
#     obj=DataIngestion()
#     obj.initiate_data_ingestion()
