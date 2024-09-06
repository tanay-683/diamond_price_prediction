import pandas as pd
import numpy as np
from src.logger.my_logging import my_logging
from src.exception.exception import customException

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import save_object, evaluate_model

from sklearn.linear_model import LinearRegression, Ridge, Lasso

class ModelTrainerConfig:
    pass


class ModelTrainer:
    def __init__(self):
        pass

    def initiate_model_training(self):
        try:
            pass
        except Exception as e:
            my_logging.info()
            raise customException(e,sys)
    
