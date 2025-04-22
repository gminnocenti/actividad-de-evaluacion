import os
import joblib
import json
import pandas as pd
import logging
from azureml.core.model import Model
from sklearn.preprocessing import OneHotEncoder


def init():
    global model

        
    model_path = Model.get_model_path('model-actividad-evaluacion')
    model = joblib.load(model_path)


def run(raw_data):
    try:
        data = json.loads(raw_data)['data'][0]
        data = pd.DataFrame(data)
        # LLamar la funcion para preprocesar los datos
        df = data.drop(columns=["NameStyle", "CustomerID", "PasswordHash", "PasswordSalt", "rowguid"])
        
        # aplicamos one hot encoder
        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        encoded_array = encoder.fit_transform(df)
        encodedx = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(df.columns))
        predictions = model.predict(encodedx)
        return json.dumps({"result": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
