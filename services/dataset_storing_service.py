import h5py
import pandas as pd

# TODO: constant here or global var for default? apply to all
def save_dataset_to_h5(training_df: pd.DataFrame, filename: str = 'airfrans_dataset.h5') -> None:
    """Save the training dataset to an HDF5 file.

    Args:
        training_df (pd.DataFrame): The dataframe to be saved.
        filename (str): The name of the HDF5 file.
    """
    with h5py.File(filename, 'w') as f:
        # TODO: separate?
        f.create_dataset('inputs', data=training_df[['x', 'y', 'sdf']])
        # Optionally add target dataset
        f.create_dataset('targets', data=training_df[['v_x', 'v_y']])
        # training_df.to_csv('output.csv', sep=';', header=True, index=False)
        
# TODO: write docstring here
# TODO: change all prints to logs
def read_dataset_from_h5(filename: str = 'airfrans_dataset.h5') -> None:
    """Save the training dataset to an HDF5 file.

    Args:
        training_df (pd.DataFrame): The dataframe to be saved.
        filename (str): The name of the HDF5 file.
    """
    # Open the HDF5 file in read mode
    with h5py.File(filename, 'r') as f:
        # List all datasets in the file
        print(f"Datasets in the file {filename}:")
        for dataset_name in f.keys():
            print(f"{dataset_name}: shape={f[dataset_name].shape}, dtype={f[dataset_name].dtype}")
        
        # Access a specific dataset (for example, 'inputs')
        inputs = f['inputs'][:]
        print("\nFirst few entries in 'inputs':")
        print(inputs[:5])  # Print the first 5 rows

        # Access another dataset (for example, 'targets')
        targets = f['targets'][:]
        print("\nFirst few entries in 'targets':")
        print(targets[:5])