import pandas as pd
import os
import sys

from src.exception.exception import customException
from src.logger.my_logging import get_logger
# time to load the model
from src.utils.utils import load_object


logger = get_logger()


class PredictPipeline:

    def __init__(self):
        print("initiated...prediction")

    def predict(self):
        try:
            
        except Exception as e:
            raise customException(e, sys)