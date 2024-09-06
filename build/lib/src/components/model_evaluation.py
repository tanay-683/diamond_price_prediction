import pandas as pd
import numpy as np
from src.logger.my_logging import my_logging
from src.exception.exception import customException

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            my_logging.info()
            raise customException(e,sys)
    
