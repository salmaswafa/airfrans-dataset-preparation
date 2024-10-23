import airfrans as af
import logging
from typing import List

import config.globals as globals

def load_simulation_names(task: str = 'full', train: bool = True, output_file: str = globals.TRAINING_DATASET_NAMES_FILENAME) -> None:
    """Load dataset names from the dataset and save them to a text file.

    Args:
        task (str): The type of task to load the dataset for (default is 'full'). Other ones are 'reynolds' for shorter datasets
        train (bool): Whether to load the training dataset (default is True). False loads test dataset.
        output_file (str): The name of the file to save the dataset names to (default is 'training_dataset_names.txt').
    """
    # Load the simulation names using the airfrans API
    _, dataset_names = af.dataset.load(root=str(globals.DATASET_PATHS[globals.ENV]['DIRECTORY_PATH'] / globals.DATASET_PATHS[globals.ENV]['DATASET_FOLDER_NAME']), 
                                                  task=task, train=train)

    # Save the simulation names to the output file
    with open(output_file, "w") as file:
        for dataset_name in dataset_names:
            file.write(dataset_name + "\n")
    
    # Log the completion of dataset name saving
    logging.info(f"Dataset names saved to {output_file}")

def load_all_simulations_names() -> None:
    """Load simulation names from both the training and test datasets from their respective files.
    """
    load_simulation_names(train = True, output_file = globals.TRAINING_DATASET_NAMES_FILENAME)
    load_simulation_names(train = False, output_file = globals.TEST_DATASET_NAMES_FILENAME)

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