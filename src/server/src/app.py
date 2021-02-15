from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#listOfTegs = []


@app.route("/gettingTags", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def gettingTags():
    text = request.get_json()
    result = ["ass", "cock", "fuck", "semen"]
    #for i in listOfTegs:
     #   for j in result:
      #      if j["vector"] < i["vector"]:
       #         j = i
    # print(text)
    return jsonify(hashtags=result)


def main():
    app.run(port=5050, debug=True)


if __name__ == "__main__":
    main()
