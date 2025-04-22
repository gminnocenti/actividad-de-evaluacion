import pandas as pd
import json
import requests
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

#cargar dataset y remover la columna que vamos a predecir
data = pd.read_csv("customers.csv")#(input_data)
# extraer las primeras 5 filas para probar el api
df = data.head(5)
df['y'] = pd.to_datetime(df['ModifiedDate']).map(pd.Timestamp.toordinal)
#guardar valores reales
y= df['y'].to_list()
df.drop(['y'], axis=1, inplace=True)

data_dict = df.to_dict(orient='list')
#Formateado para la API:
data_json = json.dumps({"data": [data_dict]})
# abrir uri json
suri = open("uri.json", "r")
scoring_uri = json.load(suri)["URI"]
suri.close()


headers = {"Content-Type": "application/json"}
response = requests.post(scoring_uri, data=data_json, headers=headers)

if response.status_code == 200:
    result = json.loads(response.json())
    #resultados de la prediccion
    print("Resultados de la prediccion: \n")
    predicted_values = result['result']
    print(predicted_values)
    data["Exited"] = result
    
else:
  print(f"Error: {response.text}")

print("valores reales: \n")
print(y)
#evaluar el modelo
mse = mean_squared_error(y, predicted_values)
r2 = r2_score(y, predicted_values)
print(f"R^2: {r2}")
print(f"MSE: {mse}")
# convertir predicciones a formato fecha
df = pd.DataFrame(predicted_values, columns=["Fecha_predicha"])
df['Fecha_predicha'] = df['Fecha_predicha'].apply(lambda x: pd.Timestamp.fromordinal(int(x)))
# imprimir predicciones en formato fecha
print("Predicciones en formato fecha: \n") 
print(df['Fecha_predicha'].to_list())