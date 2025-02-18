import pandas as pd

wildfires_csv = pd.read_csv("data/wildfires.csv")
print(wildfires_csv['incident_longitude'].head())