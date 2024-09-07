import os, sys
import pandas as pd

from src.exception.exception import customException
from src.logger.my_logging import get_logger
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


logger = get_logger()

obj = DataIngestion()

data_transformation_obj = DataTransformation()

model_trainer_obj = ModelTrainer()


train_data_path, test_data_path = obj.initiate_data_ingestion()

train_arr, test_arr = data_transformation_obj.initiate_data_transformation(
    train_data_path, test_data_path
)

model_trainer_obj.initiate_model_training(train_arr, test_arr)
