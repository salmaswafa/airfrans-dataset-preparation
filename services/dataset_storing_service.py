import h5py
import pandas as pd

def save_dataset_to_h5(training_df: pd.DataFrame, filename: str = 'airfrans_dataset2.h5') -> None:
    """Save the training dataset to an HDF5 file.

    Args:
        training_df (pd.DataFrame): The dataframe to be saved.
        filename (str): The name of the HDF5 file.
    """
    with h5py.File(filename, 'w') as f:
        # TODO: separate?
        f.create_dataset('inputs', data=training_df)
        # Optionally add target dataset
        # f.create_dataset('targets', data=targets)
        # training_df.to_csv('output.csv', sep=';', header=True, index=False)