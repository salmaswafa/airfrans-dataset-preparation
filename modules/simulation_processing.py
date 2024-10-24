import logging
import airfrans as af
import pandas as pd
from typing import Dict

import config.globals as globals
from modules.dataset_loading import read_dataset_names

def process_simulation_dataset(dataset_name: str) -> pd.DataFrame:
    """Process a single simulation and extract relevant data.

    Args:
        dataset_name (str): The name of the simulation to process.

    Returns:
        pd.DataFrame: A dataframe containing the simulation data.
        
    Raises:
        ValueError: If the simulation cannot be loaded or has invalid data.
    """
    
    try:
        simulation = af.Simulation(root=str(globals.DATASET_PATHS[globals.ENV]['DIRECTORY_PATH'] / globals.DATASET_PATHS[globals.ENV]['DATASET_FOLDER_NAME']), name=dataset_name, T=298.15)

        simulation_data: Dict[str, pd.Series] = {
            'x': simulation.position[:, 0],
            'y': simulation.position[:, 1],
            'sdf': simulation.sdf[:, 0],
            'v_x': simulation.velocity[:, 0],
            'v_y': simulation.velocity[:, 1]
        }

        return pd.DataFrame(simulation_data)
    
    except Exception as e:
        logging.error(f"Error processing simulation {dataset_name}: {e}")
        raise ValueError(f"Failed to process simulation: {dataset_name}") from e

def process_all_simulation_datasets(input_file: str = globals.TRAINING_DATASET_NAMES_FILENAME) -> pd.DataFrame:
    """Process all simulations and extract relevant data.

    Args:
        input_file (str): The name of the file with the dataset simulation folder names.

    Returns:
        pd.DataFrame: A dataframe containing all simulation data (the whole dataset).
    """
    
    dataset_names: list[str] = read_dataset_names(input_file)
    full_df: pd.DataFrame = pd.DataFrame()
    
    for i, dataset_name in enumerate(dataset_names):
        if i % 100 == 0:  # Log every 100 iterations
            logging.info(f"Processing dataset {i+1}/{len(dataset_names)}: {dataset_name}")

        # Process simulation data
        simulation_df: pd.DataFrame = process_simulation_dataset(dataset_name)
        full_df: pd.DataFrame = pd.concat([full_df, simulation_df])

        # Break for testing purposes, comment this out for full processing
        # break
    
    return full_df
