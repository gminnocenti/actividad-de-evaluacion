from preprocessing import preprocess_and_split_data
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle
#cargar datos que fuerron previamente guardados al conectarse a la base de datos de sql de azure en el archivo connection_sql_database.py
data = pd.read_csv('customers.csv')
#mandar a llamar funcion del archivo preprocessing.py
X_train, X_test, y_train, y_test = preprocess_and_split_data(data)
#usar xgboost para entrenar el modelo
model = XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"R^2: {r2}")
print(f"MSE: {mse}")
#guardar modelo formato pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
