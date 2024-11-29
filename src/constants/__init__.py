import os 
import sys
from datetime import datetime


"""
#two options for creating directories in artifacts:
# 1. artifacts -> pipeline folder -> timestamp -> output
# 2. artifacts -> pipeline folder -> output
to understant the flow, see the notes --> constants_notes.txt
"""

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "data"
DATA_DIR_KEY = "air_flight.csv"

"""
Three stages of file creation in artifacts:
1. Name of the process (i.e; data ingestion)
2. Nmae of the directory (i.e; raw data directory) where the data will be cloned and saved
3. Name of the directory 2 (i.e; ingested data directory) where splited data will be saved
"""

ARTIFACT_DIR_KEY = "artifacts"

#data ingestion related variable
DATA_INGESTION_KEY ="data ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw data directory"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested data directory"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"


#here we will be creating the preprocessing pickle file
#data Transformation related variable
DATA_TRANSFORMATION_ARTIFACT = "data transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMTION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"
#os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT,
       #                                  DATA_TRANSFORM_DIR)


#here we will be creating our pickle file for best model
#model Training related variable 
MODEL_TRAINER_KEY = "model trainer"
MODEL_OBJECT = "model.pkl"