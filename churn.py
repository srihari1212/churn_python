import pandas as pd
#conda env churn
data = pd.read_csv("customer_churn_data.csv")
print(data.head())
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'],errors='coerce')

data['TotalCharges'] = data['TotalCharges'].astype("float")