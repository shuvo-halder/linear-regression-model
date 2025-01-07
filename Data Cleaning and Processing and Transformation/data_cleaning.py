import pandas as pd
import numpy as np
import os

file_name = "Data Cleaning and Processing and Transformation/data.csv"
script_dir = os.getcwd()
# Load the data
data = pd.read_csv(os.path.normcase(os.path.join(script_dir, file_name)))

data.dropna(inplace=True)

data.fillna(data.mean(), inplace=True)
