<<<<<<< HEAD
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
=======
from flask import Flask, request, jsonify
>>>>>>> e24b0bbb0d3fa8b38b150e9b0b4e6bc2ae863efc

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

<<<<<<< HEAD

@app.route("/gettingTags", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def gettingTags():
    #print("request.data")
    text = request.get_json()
    #print(text)
    return jsonify(
        hashtags="fuck u"
=======
@app.route("/gettingTags", methods=['GET'])
def gettingTags():
    text = request.args['text']
    return jsonify(
        result=(bool)(text),
        hashtags=text
>>>>>>> e24b0bbb0d3fa8b38b150e9b0b4e6bc2ae863efc
    )


def main():
    app.run(port=5050, debug=True)

if __name__ == "__main__":
    main()
