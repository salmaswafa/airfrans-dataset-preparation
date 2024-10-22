import airfrans as af
import logging
from typing import List

import globals
# TODO: get training and dataset
# TODO: better naming
def load_dataset_names(task: str = 'full', train: bool = True, output_file: str = "dataset_names.txt") -> None:
    """Load dataset names from the given directory and save them to a file.

    Args:
        task (str): The type of task to load the dataset for (default is 'full').
        train (bool): Whether to load the training datasets (default is True).
        output_file (str): The name of the file to save the dataset names to (default is 'dataset_names.txt').
    """
    # Load the dataset names using the airfrans API
    # TODO: check this underscore !
    _, dataset_names = af.dataset.load(root=str(globals.dataset_directory_path / globals.dataset_folder_name), 
                                                  task=task, train=train)

    # Save the dataset names to the output file
    with open(output_file, "w") as file:
        for dataset_name in dataset_names:
            file.write(dataset_name + "\n")
    
    # Log the completion of dataset name saving
    logging.info(f"Dataset names saved to {output_file}")

def read_dataset_names(input_file: str = "dataset_names.txt") -> List[str]:
    """Read the dataset names from a file and return them as a list.

    Args:
        input_file (str): The file containing dataset names (default is 'dataset_names.txt').

    Returns:
        List[str]: A list of dataset names.
    """
    with open(input_file, "r") as file:
        dataset_names = [line.strip() for line in file]
    
    return dataset_names