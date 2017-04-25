from flask import Flask, render_template, request
import requests
import json
from classifier import trainedNBClassifier, extract_features

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test", methods=['POST'])
def test():
    if request.method == 'POST':
        # text = request.form['userinput']
        # print(text)
        r = requests.get("http://content.guardianapis.com/search?api-key=test")
        headlines = json.loads(r.text)['response']['results']
        # print(headlines)
        results = []
        lines = []
        for headline in headlines:
            lines.append(headline["webTitle"])
        print(lines)
        for line in lines:
            problemInstance = line.split()
            problemFeatures = extract_features(problemInstance)
            result = trainedNBClassifier.classify(problemFeatures)
            results.append(result)
        send = zip(lines, results)
        print(send)
    return render_template('test.html', send=send)

if __name__ == '__main__':
    app.debug = True
    app.run()
