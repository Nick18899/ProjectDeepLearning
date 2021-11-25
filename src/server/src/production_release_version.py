import os
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
import flask_cors
from bert_serving.client import BertClient
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import tensorflow as tf
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import MultiLabelBinarizer

def generate_mlb() -> MultiLabelBinarizer:
    file = open('./tags.txt', 'r')
    tags = set(file.read().splitlines())
    print(tags, len(tags))
    mlb = MultiLabelBinarizer()
    mlb.fit([tags])
    print(mlb.classes_, len(mlb.classes_))
    file.close()
    return mlb

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/gettingTags", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def gettingTags():
    text = request.get_json()
    print(text)
    s = text['value']
    mlb = generate_mlb()
    bertClient = BertClient()
    dependincies = {
        'precision': keras.metrics.Precision(),
        'recall': keras.metrics.Recall(),
        'binary_precision': keras.metrics.Precision(),
        'binary_recall': keras.metrics.Recall()
    }
    model = tf.keras.models.load_model('./tag_prediction_model.h5', custom_objects=dependincies)
    model_with_likes = tf.keras.models.load_model('./tag_prediction_model_with_likes.h5')
    s = bertClient.encode([s])
    pr = model.predict([[s]])
    pr = pr[0][0]
    ind = np.argpartition(pr, -30)[-30:]
    pred = np.zeros(len(pr))
    for i in range(0, len(pred)):
        if i in ind:
          pred[i]=1
    x = np.concatenate(([pred],[np.zeros(len(pred))]), axis = 0)
    list_of_corresponding_tags =  mlb.inverse_transform(x)
    list_of_corresponding_tags = list(list_of_corresponding_tags[0])
    list_of_corresponding_tags = sorted([(np.dot(pr, mlb.transform([[tag]])[0]),
        model_with_likes.predict([[s[0]],[mlb.transform([[tag]])[0]]])[0][0], tag) for tag in list_of_corresponding_tags], reverse=True)
    return jsonify(hashtags=[tag[2] for tag in list_of_corresponding_tags][:(int)(text['number'])])

@app.route("/")
@cross_origin()
def world():
    return jsonify(hashtags=['Hello', 'World'])



def main():
    app.run(host='0.0.0.0', port=5050, debug=True)


if __name__ == "__main__":
    main()
