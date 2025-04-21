import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def preprocess_and_split_data(df: pd.DataFrame):
    df = df.drop(columns=["NameStyle", "CustomerID", "PasswordHash", "PasswordSalt", "rowguid"])

    x = df.drop(columns=["ModifiedDate"]) 

    # aplicamos one hot encoder
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded_array = encoder.fit_transform(x)
    encodedx = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(x.columns))
    return encodedx