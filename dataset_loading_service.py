from pathlib import Path
import airfrans as af

directory_path = Path('./')
folder_name = './Dataset'

# TODO: get training and test
# TODO: better naming
def load_dataset_names():
    """_summary_
    """
    dataset_list, dataset_names = af.dataset.load(root=str(directory_path/folder_name), task = 'full', train = True)
    with open("dataset_names.txt", "w") as file:
        for dataset_name in dataset_names:
            file.write(dataset_name + "\n")

def read_dataset_names():
    with open("dataset_names.txt", "r") as file:
        dataset_names = [line.strip() for line in file]
    return dataset_names