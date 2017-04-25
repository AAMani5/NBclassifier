from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test", methods=['POST'])
def test():
    if request.method == 'POST':
        r = requests.get("http://content.guardianapis.com/search?api-key=test")
        headlines = json.loads(r.text)['response']['results']
        # print(headlines)
        text = request.form['userinput']
        # print(text)
    return render_template('test.html', text=text, headlines=headlines)

if __name__ == '__main__':
    app.debug = True
    app.run()
