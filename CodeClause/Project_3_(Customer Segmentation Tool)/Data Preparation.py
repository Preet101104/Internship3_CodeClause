import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('customer_data.csv')

# Drop missing values
data.dropna(inplace=True)

# Encode categorical variables
data = pd.get_dummies(data, columns=['gender', 'marital_status'])

# Scale numerical variables
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data[['age', 'income']] = scaler.fit_transform(data[['age', 'income']])
