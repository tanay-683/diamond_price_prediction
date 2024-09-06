import os, sys
import pandas as pd

from src.excetion.exception import custom_exception
from src.logger.my_logging import get_logger
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import model_trainer


logger = get_logger()

obj = DataIngestion()