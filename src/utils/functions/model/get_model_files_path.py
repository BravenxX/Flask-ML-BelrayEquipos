import os

def get_model_files_path(model_path, model_id, file):
    return os.path.abspath(f"{model_path}/model_{model_id}/{file}")