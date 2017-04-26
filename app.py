from flask import Flask, render_template, request
import requests
import json
import pickle


f = open('twitter_classifier.pickle', 'rb')
trainedNBClassifier = pickle.load(f)
f.close()

vocabulary_file = open('vocabulary.pickle', 'rb')
vocabulary = pickle.load(vocabulary_file)
vocabulary_file.close()

app = Flask(__name__)

def extract_features(review):
  review_words=set(review)
  features={}
  for word in vocabulary:
      features[word]=(word in review_words)

  return features

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test", methods=['POST'])
def test():
    if request.method == 'POST':
        text = request.form['userinput']
        problemInstance = text.split()
        problemFeatures = extract_features(problemInstance)
        result = trainedNBClassifier.classify(problemFeatures)
    return render_template('test.html', text=text, result=result)

if __name__ == '__main__':
    app.debug = True
    app.run()
