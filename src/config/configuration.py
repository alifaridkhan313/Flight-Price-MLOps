import os 
import sys

from src.constants import *

"""
This is the file responsible for joining the paths
more modular and simpler than that of consatnats file. 
making the file more simpler to understand annd interpret
"""

ROOT_DIR = ROOT_DIR_KEY
#ROOT_DIR = operating system get current working directory (os.getcwd)


# Dataset_url:

DATASET_PATH = os.path.join(
    ROOT_DIR, 
    DATA_DIR, 
    DATA_DIR_KEY
    )

RAW_FILE_PATH = os.path.join(
    ROOT_DIR, 
    ARTIFACT_DIR_KEY, 
    DATA_INGESTION_KEY, 
    DATA_INGESTION_RAW_DATA_DIR, 
    RAW_DATA_DIR_KEY
    )


TRAIN_FILE_PATH = os.path.join(
    ROOT_DIR, 
    ARTIFACT_DIR_KEY, 
    DATA_INGESTION_KEY,
    DATA_INGESTION_INGESTED_DATA_DIR_KEY, 
    TRAIN_DATA_DIR_KEY
    )


TEST_FILE_PATH = os.path.join(
    ROOT_DIR, 
    ARTIFACT_DIR_KEY, 
    DATA_INGESTION_KEY, 
    DATA_INGESTION_INGESTED_DATA_DIR_KEY, 
    TEST_DATA_DIR_KEY
    )


# Data Transformation steps:


PREPROCESSING_OBJ_FILE = os.path.join(
    ROOT_DIR, 
    ARTIFACT_DIR_KEY, 
    DATA_TRANSFORMATION_ARTIFACT, 
    DATA_PREPROCESSED_DIR, 
    DATA_TRANSFORMTION_PROCESSING_OBJ
    )

TRANSFORM_TRAIN_FILE_PATH = os.path.join(
    ROOT_DIR, 
    ARTIFACT_DIR_KEY, 
    DATA_TRANSFORMATION_ARTIFACT,
    DATA_TRANSFORM_DIR, 
    TRANSFORM_TRAIN_DIR_KEY
    )


TRANSFORM_TEST_FILE_PATH = os.path.join(
    ROOT_DIR, 
    ARTIFACT_DIR_KEY, 
    DATA_TRANSFORMATION_ARTIFACT,
    DATA_TRANSFORM_DIR, 
    TRANSFORM_TEST_DIR_KEY
    )



FEATURE_ENGINEERING_OBJECT_FILE_PATH = os.path.join(
    ROOT_DIR, 
    ARTIFACT_DIR_KEY, 
    DATA_TRANSFORMATION_ARTIFACT,
    DATA_PREPROCESSED_DIR, 'feature_enginnering.pkl')


# Model Training steps:


MODEL_FILE_PATH = os.path.join(
    ROOT_DIR, 
    ARTIFACT_DIR_KEY, 
    MODEL_TRAINER_KEY, 
    MODEL_OBJECT
    )