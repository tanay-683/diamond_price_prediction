# model_trainer me humne thoda sa evaluation kiya tha but yaha hum mlflow ki help se model evaluation karenge
# we used train data to train the model and test data to evaluate the model
import mlflow
import os, sys
import numpy as np
import pickle
import mlflow.sklearn 
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


from src.utils.utils import load_object 
from src.exception.exception import customException
from src.logger.my_logging import get_logger

logger = get_logger()

class ModelEvaluation:
    def __init__(self):
        logger.info("evaluation started !!!")
    
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        logger.info("evaluation metrics captured")
        return rmse, mae, r2

    def initiate_model_evaluation(self, train_data, test_data):
        try:
            x_test, y_test = test_data[:,:-1], test_data[:,-1]
            # load the model
            model_path = os.path.join("artifacts", "model.pkl")
            model = load_object(model_path)


            # mlflow.set_registry_uri("")# demands path where your model will be saved, can be a cloud location or local

            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            print(tracking_url_type_store)

            # start the mlflow server
            with mlflow.start_run():
                # predict the test data
                y_pred = model.predict(x_test)

                rmse, mae, r2 = self.eval_metrics(y_test, y_pred)
                
                # log the metrics
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)


        except Exception as e:
            logger.error("Error occured in initiate_model_evaluation method")
            raise customException(e, sys)