import time
import logging
from typing import List, Tuple, Dict
import globals

from services.dataset_loading_service import load_datasets_names
from services.logging_service import setup_logging
from services.simulation_processing_service import process_simulation_datasets
from services.data_visualization_service import visualize_simulation
from services.stats_calculation_service import calculate_statistics
from services.dataset_storing_service import read_dataset_from_h5, save_dataset_to_h5

# TODO: add more typing here?

def main() -> None:
    """Main function to orchestrate dataset processing."""
    setup_logging()
    logging.info("Starting the program")

    start_time = time.time()
    
    # TODO: keep as df or make it an array for faster processing?
    training_df = process_simulation_datasets(globals.training_dataset_names_filename)
    test_df = process_simulation_datasets(globals.test_dataset_names_filename)
    
    # TODO: where do you want to put this?
    # Visualize one simulation (optional)
    # Uncomment the following line if you want to visualize each dataset
    # visualize_simulation(simulation)

    # Calculate and print statistics
    calculate_statistics(training_df)

    # Save the dataset to an HDF5 file
    save_dataset_to_h5(training_df, globals.training_dataset_filename)
    save_dataset_to_h5(test_df, globals.test_dataset_filename)
    
    # checking structure
    # TODO: validate when done on databricks
    # read_dataset_from_h5(globals.training_dataset_filename)
    # read_dataset_from_h5(globals.test_dataset_filename)

    logging.debug(training_df.head())
    logging.debug(test_df.head())
    print(f'Time taken: {time.time() - start_time:.2f} seconds')

if __name__ == "__main__":
    # Run only once - already run and filenames stored for efficiency
    # TODO: add a note to uncomment it or keep it or push files?
    # load_datasets_names()
    
    main()