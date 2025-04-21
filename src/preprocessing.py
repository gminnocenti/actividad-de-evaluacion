import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def preprocess_and_split_data(df: pd.DataFrame):
    df = df.drop(columns=["NameStyle", "CustomerID", "PasswordHash", "PasswordSalt", "rowguid"])

    y = df["ModifiedDate"]
    x = df.drop(columns=["ModifiedDate"]) 

    # aplicamos one hot encoder
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded_array = encoder.fit_transform(x)
    encodedx = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(x.columns))

    # transformamos variable objetivo a valor numérico
    y = pd.to_datetime(y)
    y = (y - y.min()).dt.days

    x_train, x_test, y_train, y_test = train_test_split(encodedx, y, test_size=0.2, random_state=7)
    return x_train, x_test, y_train, y_test
