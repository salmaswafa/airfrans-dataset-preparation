import time
import logging
import config.globals as globals
import pandas as pd

from modules.logging import setup_logging
from modules.dataset_loading import load_all_simulations_names
from modules.simulation_processing import process_all_simulation_datasets
from modules.dataset_storage import save_dataset_to_csv, save_dataset_to_table

def main() -> None:
    """Main function to orchestrate dataset processing."""
    setup_logging()
    logging.info("Starting the program")
    start_time = time.time()
    
    # Run only once - already run and filenames stored in .txt files for efficiency. Uncomment to reload.
    if globals.LOAD_SIMULATION_NAMES:
        load_all_simulations_names()
    
    # process datasets to extract wanted to datapoints
    training_df: pd.DataFrame = process_all_simulation_datasets(globals.TRAINING_DATASET_NAMES_FILENAME)
    test_df: pd.DataFrame = process_all_simulation_datasets(globals.TEST_DATASET_NAMES_FILENAME)

    if globals.ENV == globals.Environment.LOCAL:
        save_dataset_to_csv(df = training_df, filename = globals.TRAINING_DATASET_OUTPUT_FILENAME)
        save_dataset_to_csv(df = test_df, filename = globals.TEST_DATASET_OUTPUT_FILENAME)
    elif globals.ENV == globals.Environment.CLOUD:
        # Save the datasets to delta tables on databricks
        save_dataset_to_table(df = training_df, table_path = globals.AIRFRANS_TRAINING_TABLE_PATH)
        save_dataset_to_table(df = test_df, table_path = globals.AIRFRANS_TEST_TABLE_PATH)
    
    logging.info(f'Time taken: {time.time() - start_time:.2f} minutes')

if __name__ == "__main__":
    main()