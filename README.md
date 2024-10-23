# airfRANS Dataset Preparation

## Overview

This project prepares a dataset for training a machine learning model using the airfRANS dataset. The dataset contains RANS simulation solutions of various airfoils, which will be processed to extract relevant features for machine learning applications.

## Objective

The primary objective is to create a dataset that includes:

	•	Input features: A sequence of points represented by their coordinates (x,y) and the signed distance (SDF) value.
	•	Target variables: The velocity components (v_x, v_y).

This dataset will facilitate quick loading for model training by processing the dataset and storing it into Delta tables on Databricks.

## Structure

The project is organized into several modules, each responsible for specific tasks:

	•	Logging: Handles the logging configuration and output.
	•	Dataset Loading: Responsible for loading simulation names.
	•	Simulation Processing: Processes individual simulations and compiles the datasets.
	•	Dataset Storage: Manages saving the processed datasets either as CSV files for local environments or as Delta tables for cloud environments.

## Requirements

You can install the required libraries using pip:

`pip install -r requirements.txt`

Note: On Databricks (cloud environment), this is done automatically in the cluster so you don't need to do it.

## Usage

	1.	Set Up Environment: Define the environment in which you want to run the script (LOCAL or CLOUD) in ENV in config/globals.py.
	2.	Load Simulation Names: Initially, you may want to run the function load_all_simulations_names() to save the dataset names to text files. This function was already run in advance for efficiency and faster testing to avoid redundant tasks. Set the value to True or False depending on whether you want to reload it or not in LOAD_SIMULATION_NAMES in config/globals.py.
	3.	Run the Program: Execute main.py:

`python main.py`

The program will:

	•	Set up logging.
	•	Load dataset names from the specified text files (if required)
	•	Process the simulations to extract the necessary datapoints.
	•	Save the output as either CSV files or Delta tables, depending on the environment.

## Design Decisions

	•	Separation of Concerns: Each module has a specific responsibility, making the code modular and easier to maintain.
	•	Environment Configuration: Using an enumeration (Environment) to manage different environments simplifies switching between local and cloud setups.
	•	Logging: Implemented comprehensive logging to track the progress and any issues during execution.
	•	Data Handling: The processed dataset can be saved in different formats (CSV for local and Delta for cloud) to accommodate various use cases.

## Conclusion

This project provides a structured approach to preparing the airfRANS dataset for machine learning. It can be extended and modified based on specific requirements or additional functionalities.

For further information on the airfRANS dataset and the associated Python library, please refer to the official documentation:
https://airfrans.readthedocs.io/en/latest/index.html