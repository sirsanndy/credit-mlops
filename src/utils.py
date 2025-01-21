import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

def load_data(fname: str):
   data = pd.DataFrame(pd.read_csv(fname), index=None)
   print(f'Data Shape: {data.shape}')
   return data

def split_input_output(data, target_col):
    X = data.drop(columns=[target_col])
    y = data[target_col]
    
    print(f"Original data shape: {data.shape}")
    print(f"X data shape: {X.shape}")
    print(f"y data shape: {y.shape}")
    
    return X, y

def split_train_test(X, y, test_size, random_state=None):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    
    print(f"X train shape: {X_train.shape}")
    print(f"X test shape: {X_test.shape}")
    print(f"y train shape: {y_train.shape}")
    print(f"y test shape: {y_test.shape}")
    
    return X_train, X_test, y_train, y_test

def serialize_data(data, path):
    joblib.dump(data, path)
    print(f"Data telah diserialisasi ke {path}")

def deserialize_data(path):
    data = joblib.load(path)
    return data