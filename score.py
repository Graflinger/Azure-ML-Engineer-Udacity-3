import joblib
import numpy as np
import os

# The init() method is called once, when the web service starts up.


def init():
    global model

    # The AZUREML_MODEL_DIR environment variable indicates
    # a directory containing the model file you registered.
    model_filename = 'best_model_hyperdrive.pkl'
    model_path = os.path.join(os.environ['AZUREML_MODEL_DIR'], model_filename)

    model = joblib.load(model_path)


def run(data):
    # temp = json.loads(data)
    # data = pd.DataFrame(temp['data'])
    result = model.predict(data)
    # You can return any data type, as long as it is JSON serializable.
    return result.tolist()
