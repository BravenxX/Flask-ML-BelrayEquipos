from flask import Flask, jsonify, request

import numpy as np
import json

from config import MODELS_MACHINARY_ELEMENTS_DIR
from utils.functions.model.get_model_values import get_model_values

app = Flask(__name__)

@app.route("/", methods=["GET"])
def say_hello():
    return jsonify({"system": "Analisis y predicción de quipos Belray."})

@app.route("/api/v1/predictions/machinery_elements/<model_id>", methods=["GET"])
def get_prediction(model_id):

    model, X_scaler, y_scaler = get_model_values( MODELS_MACHINARY_ELEMENTS_DIR, model_id)

    sample_to_evalue = []
    for i in request.args:
        sample_to_evalue.append(request.args.get(i))

    sample_to_evalue = np.array(sample_to_evalue, dtype=np.float64).reshape(1, -1)
    sample_to_evalue = X_scaler.transform(sample_to_evalue)

    prediction = model.predict(sample_to_evalue)

    prediction = y_scaler.inverse_transform(prediction)
    prediction = prediction[0][0]

    return jsonify({"Fe": json.dumps(prediction.astype(float))})

if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True)
