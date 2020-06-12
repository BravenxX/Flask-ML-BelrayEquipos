
import joblib
import tensorflow as tf

from utils.functions.model.get_tf_model import get_tf_model
from utils.functions.model.get_model_files_path import get_model_files_path 

def get_model_values(model_path, model_id):
    X_scaler_path = get_model_files_path(model_path, model_id, "scaler_X.save")
    y_scaler_path = get_model_files_path(model_path, model_id, "scaler_y.save")

    architecture_model_path = get_model_files_path(model_path, model_id, "architecture.json")
    weight_model_path = get_model_files_path(model_path, model_id, "weight.h5")

    X_scaler = joblib.load(X_scaler_path)
    y_scaler = joblib.load(y_scaler_path)

    model = get_tf_model(architecture_model_path, weight_model_path)

    return model, X_scaler, y_scaler

