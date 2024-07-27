import pandas as pd
from sklearn import datasets

def get_data():
    # Load the iris data from scikit learn
    data = datasets.load_iris()
    X, y = data.data, data.target
    return X, y

def split_train_test(X, y, test_size=0.2):
    from sklearn.model_selection import train_test_split
    return train_test_split(X, y, test_size=test_size, random_state=42)

# Esto es un comentario para comprobar cambios de linea en checkouts