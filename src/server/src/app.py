from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/gettingTags", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def gettingTags():
    text = request.get_json()
    #print(text)
    return jsonify(
        hashtags="fuck u")


def main():
    app.run(port=5050, debug=True)


if __name__ == "__main__":
    main()
