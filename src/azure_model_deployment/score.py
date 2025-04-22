import os
import joblib
import json
import pandas as pd
from azureml.core.model import Model
from sklearn.preprocessing import OneHotEncoder

def init():
    global model
    model_path = Model.get_model_path('model')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        df = pd.DataFrame(data)

        df = df.drop(columns=["NameStyle", "CustomerID", "PasswordHash", "PasswordSalt", "rowguid"])

        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        encoded_array = encoder.fit_transform(df)
        encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(df.columns))

        predictions = model.predict(encoded_df)
        return json.dumps({"result": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
