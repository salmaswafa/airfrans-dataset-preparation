import airfrans as af
import pandas as pd
import time
from dataset_loading_service import read_dataset_names

# load_dataset_names()
dataset_names = read_dataset_names()

start_time = time.time()

# TODO: Check column name conventions within the scope of ML (e.g.: prefix/suffix input/target)
training_df = pd.DataFrame()

for dataset_name in dataset_names:
  print(dataset_name)
  simulation = af.Simulation(root = './Dataset', name = dataset_name, T = 298.15)

  simulation_data = {
                      'x': simulation.position[:, 0],
                      'y': simulation.position[:, 1],
                      'sdf': simulation.sdf[:, 0],
                      'v_x': simulation.velocity[:, 0],
                      'v_y': simulation.velocity[:, 1]
                      }
    
  training_df = pd.concat([training_df, pd.DataFrame(simulation_data)])
  # break

training_df.to_csv('output.csv', sep=';', header=True, index=False)

print(f'time taken: {time.time() - start_time}')

print(training_df.head())

