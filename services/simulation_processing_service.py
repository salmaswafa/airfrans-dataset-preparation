import logging
import airfrans as af
import pandas as pd
from typing import Dict

from services.dataset_loading_service import read_dataset_names

def process_simulation_dataset(dataset_name: str) -> pd.DataFrame:
    """Process a single simulation and extract relevant data.

    Args:
        dataset_name (str): The name of the dataset to process.

    Returns:
        pd.DataFrame: A dataframe containing the simulation data.
    """
    simulation = af.Simulation(root='./Dataset', name=dataset_name, T=298.15)

    simulation_data: Dict = {
        'x': simulation.position[:, 0],
        'y': simulation.position[:, 1],
        'sdf': simulation.sdf[:, 0],
        'v_x': simulation.velocity[:, 0],
        'v_y': simulation.velocity[:, 1]
    }

    return pd.DataFrame(simulation_data)

# TODO: write docstring for this function
def process_simulation_datasets() -> pd.DataFrame:
    """Process a single simulation and extract relevant data.

    Args:
        dataset_name (str): The name of the dataset to process.

    Returns:
        pd.DataFrame: A dataframe containing the simulation data.
    """
    
    # TODO: Check column name conventions within the scope of ML (e.g.: prefix/suffix input/target)
    dataset_names = read_dataset_names()
    training_df = pd.DataFrame()
    
    for i, dataset_name in enumerate(dataset_names):
        if i % 10 == 0:  # Log every 10 iterations
            logging.debug(f"Processing dataset {i+1}/{len(dataset_names)}: {dataset_name}")

        # Process simulation data
        simulation_df = process_simulation_dataset(dataset_name)
        training_df = pd.concat([training_df, simulation_df])

        # Break for testing purposes, comment this out for full processing
        break

    return training_df