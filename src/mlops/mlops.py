import pandas as pd

def get_data():
    # Load the data from the data folder
    data = pd.read_csv('data/data.csv')
    return data