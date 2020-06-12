import tensorflow as tf

def get_tf_model(architecture_path, weights_path): 

    with open(architecture_path, 'r') as f:
        model_json = f.read()

    model = tf.keras.models.model_from_json(model_json)

    model.load_weights(weights_path)

    return model