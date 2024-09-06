import pandas as pd
import numpy as np
from src.logger.my_logging import get_logger
from src.exception.exception import customException
from src.utils.utils import save_object

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder


logger = get_logger()


class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transform(self):
        try:
            logger.info("Stating Data Transformation")

            categorical_cols = ["cut", "color", "clarity"]
            numerical_cols = ["carat", "depth", "table", "x", "y", "z"]

            cut_categories = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
            color_categories = ["D", "E", "F", "G", "H", "I", "J"]
            clarity_categories = [
                "I1",
                "SI2",
                "SI1",
                "VS2",
                "VS1",
                "VVS2",
                "VVS1",
                "IF",
            ]

            logger.info("Pipeline Initiated")

            ## Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            # Categorigal Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "ordinalencoder",
                        OrdinalEncoder(
                            categories=[
                                cut_categories,
                                color_categories,
                                clarity_categories,
                            ]
                        ),
                    ),
                    ("scaler", StandardScaler()),
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_cols),
                    ("cat_pipeline", cat_pipeline, categorical_cols),
                ]
            )

            return preprocessor

        except Exception as e:
            logger.info("Error occured in the get_data_transform")
            raise customException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logger.info("Reading train and test data complete")
            logger.info(f"Train Dataframe head :\n{train_df.head(3).to_string()}")
            logger.info(f"Test Dataframe head :\n{test_df.head(3).to_string()}")

            preprocessor_obj = self.get_data_transform()

            target_variable = "price"
            columns_todrop = [target_variable, "id"]

            input_feature_train_df = train_df.drop(columns=columns_todrop, axis=1)
            target_feature_train_df = train_df[target_variable]

            input_feature_test_df = test_df.drop(columns=columns_todrop, axis=1)
            target_feature_test_df = test_df[target_variable]

            transformed_input_feature_train_df = preprocessor_obj.fit_transform(
                input_feature_train_df
            )
            transformed_input_feature_test_df = preprocessor_obj.transform(
                input_feature_test_df
            )

            logger.info("Applying preprocessor object on training and testing datasets")

            train_arr = np.concatenate[
                transformed_input_feature_train_df, np.array(target_feature_train_df)
            ]
            test_arr = np.concatenate[
                transformed_input_feature_test_df, np.array(target_feature_test_df)
            ]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj,
            )

            logger.info("preprocessing pickle file saved")

            return (train_arr, test_arr)
        except Exception as e:
            my_logging.info()
            raise customException(e, sys)
