from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def get_text():
    text = request.args['text']
    return jsonify(
        result=True,
        hashtags=text
    )
    return text


def main():
    app.run()


if __name__ == "__main__":
    main()
