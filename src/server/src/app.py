from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
import json
import fasttext

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = fasttext.load_model('./cc.en.300.bin')


def find_most_similar_sentence_from_dataset(sentence, dataset):
    vectorized_dataset = [(sentence, model.get_sentence_vector(sentence)) for sentence in dataset]
    vectorized_sentence = model.get_sentence_vector(sentence)  # 1 sentence
    answer = 'cat'
    import numpy as np
    for (sentence, vector) in vectorized_dataset:
        if np.dot(vector, vectorized_sentence) > np.dot(model.get_sentence_vector(answer), vectorized_sentence):
            answer = sentence
    return answer


def scan_kaggle_dataset():
    import csv
    with open('kaggle_dataset.csv', newline='') as csvfile:
        cnt = 0
        spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
        sentences = [row[2] for row in spamreader]
    return sentences


def searchingTheMostSimilarTwit(sentence):
    hashtags = scan_kaggle_dataset()
    normal_tags = ["politics", "planes", "science", "study", "animal", "sport", "books", "computer", "geography", "country"]
    words = find_most_similar_sentence_from_dataset(sentence, hashtags)
    print(words)
    return words


@app.route("/gettingTags", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def gettingTags():
    text = request.get_json()
    print(text['value'])
    result = searchingTheMostSimilarTwit(text['value'])
    return jsonify(hashtags=result)


def main():
    app.run(port=5050, debug=True)


if __name__ == "__main__":
    main()
