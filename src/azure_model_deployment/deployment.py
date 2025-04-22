## STEP 1: Set up the workspace.

import json
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("KEY")



from azureml.core import Workspace
"""
ws = Workspace.create(name="actividad-de-evaluacion",
                      subscription_id = key, # remplazar por tu subsucripcion id
                      resource_group = "resource-group-actividad-evaluacion",
                      location="centralindia")

"""
ws = Workspace.get(name="actividad-de-evaluacion",
                      subscription_id = key, # remplazar por tu subsucripcion id
                      resource_group = "resource-group-actividad-evaluacion")

from azureml.core.environment import Environment
from azureml.core.model import InferenceConfig

env = Environment("env-sql")
env.python.conda_dependencies.add_pip_package("scikit-learn")   
env.python.conda_dependencies.add_pip_package("joblib")
env.python.conda_dependencies.add_pip_package("pandas")
env.python.conda_dependencies.add_pip_package("azureml-defaults")    
env.python.conda_dependencies.add_pip_package("xgboost")   

inference_config = InferenceConfig(entry_script="score.py", environment=env) #score.py esta en un archivo aparte

from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.model import Model
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

model = Model.register(workspace=ws,
                       model_path="model.pkl",  
                       model_name="model")
service = Model.deploy(workspace=ws,
                       name="actividad-evaluacion-sql",
                       models=[model],
                       inference_config=inference_config,
                       deployment_config=deployment_config,
                       overwrite=True,)

service.wait_for_deployment(show_output=True)

print(service.get_logs())

print("Scoring URI:", service.scoring_uri)

scoring_uri = service.scoring_uri
#guardar uri en un json
scoreuri = json.dumps({"URI": [scoring_uri]})
file = open("uri.json", "w")
file.write(scoreuri)
file.close()