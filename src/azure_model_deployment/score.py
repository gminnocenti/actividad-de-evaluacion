import os
import joblib
import json
import pandas as pd
import logging
from azureml.core.model import Model
from preprocessing import preprocess_data


def init():
    global model

        
    model_path = Model.get_model_path('model-actividad-evaluacion')
    model = joblib.load(model_path)


def run(raw_data):
    try:
        data = json.loads(raw_data)['data'][0]
        data = pd.DataFrame(data)
        # LLamar la funcion para preprocesar los datos
        data_df = preprocess_data(data)
        predictions = model.predict(data_df)
        return json.dumps({"result": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
