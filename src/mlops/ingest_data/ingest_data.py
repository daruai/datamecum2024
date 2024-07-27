import pandas as pd
from sklearn import datasets

def get_data():
    # Load the iris data from scikit learn
    data = datasets.load_iris()
    X, y = data.data, data.target
    return X, y