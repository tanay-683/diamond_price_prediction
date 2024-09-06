import pandas as pd
import numpy as np
from src.logger.my_logging import my_logging
from src.exception.exception import customException

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder

class DataTransformationConfig:
    pass

class DataTransformation:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            pass
        except Exception as e:
            my_logging.info()
            raise customException(e,sys)
    
