from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
import json
import fasttext

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
content = ''
is_parsed = ''
k = 0


# model = fasttext.load_model('./cc.en.300.bin')

def getFileViaPath(file_path):
    text_file = open(file_path, 'r')
    global content
    content = text_file.read()
    text_file.close()


def splitToStrings(s, size_of_strings=30):
    data = []
    for i in range(0, (len(s) // size_of_strings)):
        data.append(s[(i * size_of_strings): ((i + 1) * size_of_strings)])
    data.append(s[((len(s) // size_of_strings) - 1) * size_of_strings:])
    return data


def parseTextToArrays(size_of_strings):
    global is_parsed
    global content
    data = []
    if is_parsed == '':
        is_parsed = 'true'
        data = splitToStrings(size_of_strings, content)
    return data


def getTextViaK(num_of_char):
    return splitToStrings(num_of_char, content[k])


def writeInputTextViaGUI(text):
    global content
    content = text


@app.route("/gettingTags", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def gettingTags():
    text = request.get_json()
    print(text['value'])
    result = '''searchingTheMostSimilarTwit(text['value'])'''
    return jsonify(hashtags=result)


def main():
    app.run(port=5050, debug=True)


if __name__ == "__main__":
    main()
