from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,Normalizer,QuantileTransformer,PowerTransformer,LabelEncoder,OneHotEncoder,OrdinalEncoder,KBinsDiscretizer

import pandas as pd
import numpy as np
import os

# Load the data
file_name = "Data Cleaning and Processing and Transformation/data.csv"
script_dir = os.getcwd()
data = pd.read_csv(os.path.normcase(os.path.join(script_dir, file_name)))


scaler = StandardScaler()

df_scaled = scaler.fit_transform(data)
# print(df_scaled)
encoder = OneHotEncoder()
df_encoded = encoder.fit_transform(data[['Gender']])
print(df_encoded)