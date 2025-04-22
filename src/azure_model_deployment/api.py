import pandas as pd
import json
import requests
from sklearn.preprocessing import LabelEncoder

#cargar dataset y remover la columna que vamos a predecir
data = pd.read_csv("customers.csv")#(input_data)
# extraer las primeras 5 filas para probar el api
df = data.head(5)
df['y'] = pd.to_datetime(df['ModifiedDate']).map(pd.Timestamp.toordinal)
y= df['y'].to_list()
df = df.drop(['ModifiedDate', 'rowguid', 'PasswordHash', 'PasswordSalt'], axis=1)

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna('None')  
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop('y', axis=1)

data_dict = X.to_dict(orient='list')
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