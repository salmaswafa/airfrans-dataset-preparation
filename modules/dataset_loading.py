import airfrans as af
import logging
from typing import List

import config.globals as globals
# TODO: get training and dataset
# TODO: better naming
def load_dataset_names(task: str = 'full', train: bool = True, output_file: str = "training_dataset_names.txt") -> None:
    """Load dataset names from the given directory and save them to a file.

    Args:
        task (str): The type of task to load the dataset for (default is 'full').
        train (bool): Whether to load the training datasets (default is True).
        output_file (str): The name of the file to save the dataset names to (default is 'training_dataset_names.txt').
    """
    # Load the dataset names using the airfrans API
    # TODO: check this underscore !
    # TODO: remove print- and all prints
    print(f'PATH!!: "{str(globals.DATASET_PATHS[globals.ENV]["DIRECTORY_PATH"] / globals.DATASET_PATHS[globals.ENV]["DATASET_FOLDER_NAME"])}"')
    # print(f'PATH!!: "{str(globals.DATASET_PATHS[globals.ENV]['DIRECTORY_PATH'] / globals.DATASET_PATHS[globals.ENV]['DATASET_FOLDER_NAME'])}"')
    _, dataset_names = af.dataset.load(root=str(globals.DATASET_PATHS[globals.ENV]['DIRECTORY_PATH'] / globals.DATASET_PATHS[globals.ENV]['DATASET_FOLDER_NAME']), 
                                                  task=task, train=train)

    # Save the dataset names to the output file
    with open(output_file, "w") as file:
        for dataset_name in dataset_names:
            file.write(dataset_name + "\n")
    
    # Log the completion of dataset name saving
    logging.info(f"Dataset names saved to {output_file}")

# TODO: name too close to above one?
def load_datasets_names() -> None:
    """Load dataset names from both the training and test datasets in their respective files.
    """
    load_dataset_names(train = True, output_file = globals.TRAINING_DATASET_NAMES_FILENAME)
    load_dataset_names(train = False, output_file = globals.TEST_DATASET_NAMES_FILENAME)

def read_dataset_names(input_file: str = "training_dataset_names.txt") -> List[str]:
    """Read the dataset names from a file and return them as a list.

    Args:
        input_file (str): The file containing dataset names (default is 'training_dataset_names.txt').

    Returns:
        List[str]: A list of dataset names.
    """
    with open(input_file, "r") as file:
        dataset_names = [line.strip() for line in file]
    
    return dataset_names