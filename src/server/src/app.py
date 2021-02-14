from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route("/gettingTags", methods=['GET'])
def gettingTags():
    print("request.data")
    text = request.form.get("value")
    print(text)
    return jsonify(
        result=True,
        hashtags=text
    )


def main():
    app.run(host="127.0.0.1", port=5050, debug=True)


if __name__ == "__main__":
    main()
