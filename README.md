# Cloud Computing – Actividad Semana 2

Este repositorio contiene el desarrollo de una actividad práctica enfocada en la creación, entrenamiento y despliegue de un modelo de regresión utilizando **scikit-learn** y **Azure Machine Learning**.

##  Objetivo

Construir un flujo completo de machine learning, desde el preprocesamiento de datos hasta el despliegue del modelo en la nube.

##  Estructura del Equipo

El proyecto fue dividido en tres departamentos principales:

###  Departamento de Datos

- Archivos: `preprocessing.py`, `connection_sql_database.py`
- Funciones:
  - Conexión con base de datos SQL.
  - Limpieza, transformación y selección de características para el modelo.

###  Departamento de Modelos

- Archivo: `model.py`
- Funciones:
  - Entrenamiento de un modelo de regresión con **scikit-learn**.
  - Exportación del modelo entrenado como `model.pkl` usando **pickle**.

###  Departamento de Cómputo en la Nube

- Archivos: `deployment.py`, `api.py`, `score.py`
- Funciones:
  - Creación de un **Azure ML Workspace**, registro del modelo y despliegue como endpoint.
  - El endpoint generado se guarda en `uri.json`.
  - El archivo `api.py` prueba el endpoint cargando datos de `customers.csv` y obteniendo predicciones.

## 🧰 Tecnologías Utilizadas

- Python
- scikit-learn
- Azure Machine Learning SDK
- Pickle
- JSON
- XGBOOST
- `.env` para variables de entorno

## 📁 Estructura del Proyecto

```Directory structure:
└── actividad-de-evaluacion/
    ├── README.md
    ├── customers.csv
    ├── model.pkl
    ├── pyproject.toml
    ├── uv.lock
    ├── .python-version
    └── src/
        ├── connection_sql_database.py
        ├── model.py
        ├── preprocessing.py
        └── azure_model_deployment/
            ├── api.py
            ├── customers.csv
            ├── deployment.py
            ├── model.pkl
            ├── preprocessing.py
            └── score.py
```

## 🚀 Pasos para Ejecutar el Proyecto

1. **Clonar el repositorio.**  
   Haz un fork y clónalo en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/gminnocenti-actividad-de-evaluacion.git
   cd actividad-de-evaluacion
    ```
2. **Configurar entorno virtual e instalar dependencias**
Asegúrate de tener Python instalado, luego corre:

```bash
uv venv
uv source/bin/activate
uv sync
```
3. **Crear archivos `.env` con tus variables de entorno.**
    - En la carpeta `src/`, crea un archivo llamado `.env` con las credenciales de tu base de datos:
    ```
    SERVER=nombre_del_servidor
    DATABASE=nombre_de_la_base
    USERNAME=usuario
    PASSWORD=contraseña
    ```
    - En `src/azure_model_deployment/`, crea otro archivo `.env` con tu subscription ID de Azure:
    ```
    KEY=tu_subscription_id
    ```
4. **Entrenar el modelo.**
Desde la raíz del proyecto:
```
python src/model.py
```
5. **Desplegar el modelo en Azure.**
```
python src/azure_model_deployment/deployment.py
```
Esto creará el workspace, registrará el modelo y generará el endpoint en ```uri.json``` .
6. **Colocar el uri en un json en el directorio `src/azure_model_deployment/`**
Crear un archivo llamado uri.json en el directorio `src/azure_model_deployment/` que tenga el siguiente formato:
```
{
    "URI":"<pegar el uri>"
}
```
7. **Probar el endpoint.**
```
python src/azure_model_deployment/api.py
```
Este script cargará datos de `customers.csv` y validará el funcionamiento del endpoint.