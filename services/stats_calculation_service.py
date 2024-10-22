from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

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