import pandas as pd
import json
import requests
#cargar dataset y remover la columna que vamos a predecir
data = pd.read_csv("customers.csv")#(input_data)
# extraer las primeras 5 filas para probar el api
data = data.head(5)
#guardar valores reales para compararlos con los resultados del API
valores_reales=data.ModifiedDate
y = pd.to_datetime(valores_reales)
y = (y - y.min()).dt.days
data=data.drop(["ModifiedDate"], axis=1)

data_dict = data.to_dict(orient='list')
#Formateado para la API:
data_json = json.dumps({"data": [data_dict]})
# abrir uri json
suri = open("uri.json", "r")
scoring_uri = json.load(suri)["URI"][0]
suri.close()


headers = {"Content-Type": "application/json"}
response = requests.post(scoring_uri, data=data_json, headers=headers)

if response.status_code == 200:
    result = json.loads(response.json())
    #resultados de la prediccion
    print("Resultados de la prediccion")
    print(result)
    data["Exited"] = result
    print(data)
else:
  print(f"Error: {response.text}")

print("valores reales: \n")
print(y)