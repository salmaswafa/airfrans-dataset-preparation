import time
import logging
from typing import List, Tuple, Dict
# from joblib import Parallel, delayed
# import multiprocessing

from services.logging_service import setup_logging
from services.simulation_processing_service import process_simulation_datasets
from services.data_visualization_service import visualize_simulation
from services.stats_calculation_service import calculate_statistics
from services.dataset_storing_service import save_dataset_to_h5

def main() -> None:
    """Main function to orchestrate dataset processing."""
    setup_logging()
    logging.info("Starting the program")

    start_time = time.time()

    training_df = process_simulation_datasets()
    
    # TODO: where do you want to put this?
    # Visualize one simulation (optional)
    # Uncomment the following line if you want to visualize each dataset
    # visualize_simulation(simulation)

    # Calculate and print statistics
    calculate_statistics(training_df)

    # Save the dataset to an HDF5 file
    save_dataset_to_h5(training_df, 'airfrans_dataset2.h5')

    logging.debug(training_df.head())
    print(f'Time taken: {time.time() - start_time:.2f} seconds')

if __name__ == "__main__":
    main()