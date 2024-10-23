# Define the directory and folder paths
from enum import Enum
from pathlib import Path

# Define the Environment enum
class Environment(Enum):
    LOCAL = 'local'
    CLOUD = 'cloud'

# Active environment (can be set via an environment variable or config file)
ENV = Environment.LOCAL  # Set this dynamically based on your environment

# Environment-specific dataset paths
DATASET_PATHS = {
    Environment.LOCAL: {
        'DIRECTORY_PATH': Path('./'),
        'DATASET_FOLDER_NAME': './Dataset',
    },
    Environment.CLOUD: {
        'DIRECTORY_PATH': Path('/dbfs/mnt'),
        'DATASET_FOLDER_NAME': './dataset',
    }
}

# File names for dataset names
TRAINING_DATASET_NAMES_FILENAME = 'training_dataset_names.txt'
TEST_DATASET_NAMES_FILENAME = 'test_dataset_names.txt'

# File names for the full datasets
TRAINING_DATASET_FILENAME = 'training_dataset.csv'
TEST_DATASET_FILENAME = 'test_dataset.csv'

# Table paths for your datasets
TEST_TABLE_PATH = 'env.data.test_table'
AIRFRANS_TRAINING_TABLE_PATH = 'env.data.airfrans_training_table'
AIRFRANS_TEST_TABLE_PATH = 'env.data.airfrans_test_table'
