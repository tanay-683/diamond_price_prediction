""" this file will create the directory structure for the project"""



import os
from pathlib import Path
import logging

# Note : If you push a empty folder to git, it will not be pushed. So, to push a empty folder, you need to put a file in it.


list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py", #src folder will represent the source code of the project, other infrastructure code will be outside of this folder

    # a pipeline contain various components and all those components will be in the components folder
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",

    "src/pipelines/__init__.py", 
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",

    "src/utils/__init__.py", # utility functions will be in the utils
    "src/utils/utils.py",

    "src/logger/logging.py",
    "src/logger/__init__.py",

    "src/exception/exception.py",
    "src/exception/__init__.py",


    # Testing folder
    "tests/unit/__init__.py",
    "tests/unit/unit.py",

    "tests/integration/__init__.py",
    "tests/integration/int.py",

    "init_setup.sh",  # this file will contain the commands to setup the project like creating a virtual environment, installing the dependencies, etc.
    "requirements.txt",
    "requirements_dev.txt", # when i have to install requirements relataed to the development I'll run this file
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiment.ipynb", # for some experiments
    "app.py", # this file will contain the flask app
    "templates/index.html", # this file will contain the html code for the home page
    ".gitignore", # this file will contain the files and folders that should be ignored by git
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # if filedir is not empty
    if filedir != "":
        # create the directory if it does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}") 



    # for independent files, jo kisi folder me nahi hain, unko create karne ke liye

    # not os.path.exists(filepath): This condition checks if the file specified by the filepath variable does not exist. The os.path.exists() function is used to test whether a path exists on the filesystem. If the file does not exist, the condition evaluates to True.

    # os.path.getsize(filepath) == 0: This condition checks if the size of the file specified by the filepath variable is equal to 0. The os.path.getsize() function is used to get the size of a file in bytes. If the size of the file is 0, indicating an empty file, the condition evaluates to True.


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file