from flask import Flask, render_template, request, jsonify, session
import requests
import json
import pickle
from twitterAPI import getTweets


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

@app.route("/json")
def json():
    results = session['results']
    return jsonify(results=results)

@app.route("/test", methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        text = request.form['userinput']
        tweets = getTweets(text, "en", 100, "recent", "tweets.txt")
        results = []
        for tweet in tweets:
            problemInstance = tweet.split()
            problemFeatures = extract_features(problemInstance)
            result = trainedNBClassifier.classify(problemFeatures)
            results.append(result)
        classifications = zip(tweets, results)
        session['results'] = results
        return render_template('test.html', classifications=classifications)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
