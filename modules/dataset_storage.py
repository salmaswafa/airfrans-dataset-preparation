import pandas as pd
import config.globals as globals
from pyspark.sql import SparkSession
import logging

def save_dataset_to_table(df: pd.DataFrame, table_path: str = globals.TEST_TABLE_PATH) -> None:
    """Save the training dataset to a delta table.

    Args:
        df (pd.DataFrame): The dataframe to be saved.
        table_path (str): The path of the delta table.
    """
    # Create Spark session
    spark = SparkSession.builder.getOrCreate()
    
    logging.info(f"Started writing dataset to {table_path}")
    
    # Convert Pandas DataFrame to PySpark DataFrame (required to write to delta table)
    df = spark.createDataFrame(df)
    # Write the DataFrame to a Delta table
    df.write.format("delta").mode("overwrite").saveAsTable(table_path)

    logging.info(f"Finished writing dataset to {table_path}")
    
def save_dataset_to_csv(df: pd.DataFrame, filename: str = 'airfrans_dataset.csv') -> None:
    """Save the training dataset to an CSV file.

    Args:
        df (pd.DataFrame): The dataframe to be saved.
        filename (str): The name of the CSV file.
    """
    
    df.to_csv(filename, sep=';', header=True, index=False)