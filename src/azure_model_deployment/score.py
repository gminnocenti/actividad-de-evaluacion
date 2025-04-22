import os
import joblib
import json
import pandas as pd
from azureml.core.model import Model
from sklearn.preprocessing import LabelEncoder

def init():
    global model
    model_path = Model.get_model_path('model')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data'][0]
        df = pd.DataFrame(data)
        df['y'] = pd.to_datetime(df['ModifiedDate']).map(pd.Timestamp.toordinal)
        df = df.drop(['ModifiedDate', 'rowguid', 'PasswordHash', 'PasswordSalt'], axis=1)
        for col in df.select_dtypes(include='object').columns:
            df[col] = LabelEncoder().fit_transform(df[col])
        #dropear columna y
        df = df.drop('y', axis=1)
        predictions = model.predict(df)
        return json.dumps({"result": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
