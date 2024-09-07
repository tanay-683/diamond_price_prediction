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

    def predict(self, features):
        try:
            preprocssor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            # load object
            preprocessor = load_object(preprocssor_path)
            model = load_object(model_path)

            # transform the data
            scaled_features = preprocessor.transform(features)
            prediction = model.predict(scaled_features)
            return prediction

        except Exception as e:
            raise customException(e, sys)


class CustomData:
    def __init__(
        self,
        carat: float,
        depth: float,
        table: float,
        x: float,
        y: float,
        z: float,
        cut: str,
        color: str,
        clarity: str,
    ):

        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "carat": [self.carat],
                "depth": [self.depth],
                "table": [self.table],
                "x": [self.x],
                "y": [self.y],
                "z": [self.z],
                "cut": [self.cut],
                "color": [self.color],
                "clarity": [self.clarity],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logger.info("Dataframe Gathered")
            return df
        except Exception as e:
            logger.error("Error in get_data_as_dataframe in prediction_pipeline.py")
            raise customException(e, sys)
