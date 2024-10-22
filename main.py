import airfrans as af
import pandas as pd
import time
from dataset_loading_service import read_dataset_names
import matplotlib.pyplot as plt
import h5py
import numpy as np
import logging
from logging_service import setup_logging
from typing import List, Tuple, Dict
# from joblib import Parallel, delayed
# import multiprocessing

def process_simulation_data(dataset_name: str) -> pd.DataFrame:
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

def visualize_simulation(simulation: af.Simulation) -> None:
    """Visualize various simulation attributes using scatter plots.

    Args:
        simulation (af.Simulation): The simulation object containing data.
    """
    _, ax = plt.subplots(2, 3, figsize=(36, 12))

    # Plot position vs. velocity, pressure, sdf, nu_t, and airfoil attributes
    ax[0, 0].scatter(simulation.position[:, 0], simulation.position[:, 1], c=simulation.velocity[:, 0], s=0.75)
    ax[0, 1].scatter(simulation.position[:, 0], simulation.position[:, 1], c=simulation.pressure[:, 0], s=0.75)
    ax[0, 2].scatter(simulation.position[:, 0], simulation.position[:, 1], c=simulation.sdf[:, 0], s=0.75)
    ax[1, 0].scatter(simulation.position[:, 0], simulation.position[:, 1], c=simulation.nu_t[:, 0], s=0.75)
    ax[1, 1].scatter(simulation.airfoil_position[:, 0], simulation.airfoil_position[:, 1], c=simulation.airfoil_normals[:, 0], s=0.75)
    ax[1, 2].scatter(simulation.airfoil_position[:, 0], simulation.airfoil_position[:, 1], c=simulation.airfoil_normals[:, 1], s=0.75)

    # Add titles and labels
    ax[0, 0].set_title('Position vs. Velocity')
    ax[0, 0].set_xlabel('X Position')
    ax[0, 0].set_ylabel('Y Position')

    # Show the plot
    plt.show()

def calculate_statistics(training_df: pd.DataFrame) -> None:
    """Calculate and print statistical summaries of SDF and velocity.

    Args:
        training_df (pd.DataFrame): The dataframe containing training data.
    """
    mean_sdf = np.mean(training_df['sdf'])
    std_sdf = np.std(training_df['sdf'])
    mean_velocity = np.mean(training_df['v_x'], axis=0)
    std_velocity = np.std(training_df['v_x'], axis=0)

    print("SDF Mean:", mean_sdf, "SDF Std:", std_sdf)
    print("Velocity in x Mean:", mean_velocity, "Velocity in x Std:", std_velocity)

    # Optionally visualize the distributions
    plt.hist(training_df['sdf'], bins=50, alpha=0.5, label='SDF')
    plt.hist(training_df['v_x'], bins=50, alpha=0.5, label='v_x')
    plt.hist(training_df['v_y'], bins=50, alpha=0.5, label='v_y')
    plt.legend()
    plt.show()

def save_dataset_to_h5(training_df: pd.DataFrame, filename: str) -> None:
    """Save the training dataset to an HDF5 file.

    Args:
        training_df (pd.DataFrame): The dataframe to be saved.
        filename (str): The name of the HDF5 file.
    """
    with h5py.File(filename, 'w') as f:
        f.create_dataset('inputs', data=training_df)
        # Optionally add target dataset
        # f.create_dataset('targets', data=targets)
        # training_df.to_csv('output.csv', sep=';', header=True, index=False)

def main() -> None:
    """Main function to orchestrate dataset processing."""
    setup_logging()
    logging.info("Starting the program")

    dataset_names = read_dataset_names()
    # TODO: Check column name conventions within the scope of ML (e.g.: prefix/suffix input/target)
    training_df = pd.DataFrame()
    start_time = time.time()

    for i, dataset_name in enumerate(dataset_names):
        if i % 10 == 0:  # Log every 10 iterations
            logging.debug(f"Processing dataset {i+1}/{len(dataset_names)}: {dataset_name}")

        # Process simulation data
        simulation_df = process_simulation_data(dataset_name)
        training_df = pd.concat([training_df, simulation_df])

        # Visualize one simulation (optional)
        # Uncomment the following line if you want to visualize each dataset
        # visualize_simulation(simulation)

        # Calculate and print statistics
        calculate_statistics(training_df)

        # Break for testing purposes, comment this out for full processing
        break

    # Save the dataset to an HDF5 file
    save_dataset_to_h5(training_df, 'airfrans_dataset2.h5')

    logging.debug(training_df.head())
    print(f'Time taken: {time.time() - start_time:.2f} seconds')

if __name__ == "__main__":
    main()