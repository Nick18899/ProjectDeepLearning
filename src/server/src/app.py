from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/gettingTags", methods=['GET'])
def gettingTags():
    text = request.args['text']
    return jsonify(
        result=(bool)(text),
        hashtags=text
    )


def main():
    app.run(host="127.0.0.1", port=5050, debug=True)

if __name__ == "__main__":
    main()
