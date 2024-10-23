import time
import logging
from typing import List, Tuple, Dict
import config.globals as globals

from modules.logging import setup_logging
from modules.dataset_loading import load_datasets_names
from modules.simulation_processing import process_simulation_datasets
from modules.dataset_storage import save_dataset_to_csv, save_dataset_to_table

# TODO: add more typing here?
def main() -> None:
    """Main function to orchestrate dataset processing."""
    setup_logging()
    logging.info("Starting the program")
    start_time = time.time()
    
    # process datasets to extract wanted to datapoints
    training_df = process_simulation_datasets(globals.TRAINING_DATASET_NAMES_FILENAME)
    test_df = process_simulation_datasets(globals.TEST_DATASET_NAMES_FILENAME)

    if globals.ENV == globals.Environment.LOCAL:
        save_dataset_to_csv(df = training_df, filename = globals.TRAINING_DATASET_FILENAME)
        save_dataset_to_csv(df = test_df, filename = globals.TEST_DATASET_FILENAME)
    elif globals.ENV == globals.Environment.CLOUD:
        # Save the datasets to delta tables on databricks
        save_dataset_to_table(df = training_df, table_path = globals.AIRFRANS_TRAINING_TABLE_PATH)
        save_dataset_to_table(df = test_df, table_path = globals.AIRFRANS_TEST_TABLE_PATH)
    
    logging.info(training_df.head())
    logging.info(test_df.head())
    print(f'Time taken: {time.time() - start_time:.2f} seconds')

if __name__ == "__main__":
    # Run only once - already run and filenames stored in .txt files for efficiency
    # load_datasets_names()
    main()