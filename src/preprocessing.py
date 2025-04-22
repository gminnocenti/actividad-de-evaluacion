import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_and_split_data(df: pd.DataFrame):
    #convertir fecha a formato ordinal
    df['y'] = pd.to_datetime(df['ModifiedDate']).map(pd.Timestamp.toordinal)

    # eliminar columnas innecesarias
    df = df.drop(['ModifiedDate', 'rowguid', 'PasswordHash', 'PasswordSalt'], axis=1)
    # convertir columnas categoricas a numericas
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna('None')  
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop('y', axis=1)
    y = df['y']
    
    #usar train_test_split para dividir el dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test
