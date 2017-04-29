import nltk
import json
from nltk.corpus import twitter_samples
import pickle

positiveReviews = twitter_samples.strings('positive_tweets.json')
negativeReviews = twitter_samples.strings('negative_tweets.json')

testTrainingSplitIndex = 2500

testNegativeReviews = negativeReviews[testTrainingSplitIndex+1:]
testPositiveReviews = positiveReviews[testTrainingSplitIndex+1:]

trainingPositiveReviews = positiveReviews[:testTrainingSplitIndex]
trainingNegativeReviews = negativeReviews[:testTrainingSplitIndex]


def getVocabulary(trainingPositiveReviews, trainingNegativeReviews):
  positiveWordList = [word for line in trainingPositiveReviews for word in line.split()]
  negativeWordList = [word for line in trainingNegativeReviews for word in line.split()]
  allWordList = [item for sublist in [positiveWordList,negativeWordList] for item in sublist]
  allWordSet = list(set(allWordList))
  vocabulary = allWordSet
  return vocabulary

def getTrainingData(trainingPositiveReviews, trainingNegativeReviews):
  negTaggedTrainingReviewList = [{'review':oneReview.split(),'label':'negative'} for oneReview in trainingNegativeReviews]
  posTaggedTrainingReviewList = [{'review':oneReview.split(),'label':'positive'} for oneReview in trainingPositiveReviews]
  fullTaggedTrainingData = [item for sublist in [negTaggedTrainingReviewList,posTaggedTrainingReviewList] for item in sublist]
  trainingData = [(review['review'],review['label']) for review in fullTaggedTrainingData]
  return trainingData



def extract_features(review):
  review_words=set(review)
  features={}
  for word in vocabulary:
      features[word]=(word in review_words)
  return features


def getTrainedNaiveBayesClassifier(extract_features, trainingData):
  trainingFeatures=nltk.classify.apply_features(extract_features, trainingData)
  trainedNBClassifier=nltk.NaiveBayesClassifier.train(trainingFeatures) # Train the Classifier
  return trainedNBClassifier, trainingFeatures

vocabulary = getVocabulary(trainingPositiveReviews, trainingNegativeReviews)
# trainingData = getTrainingData(trainingPositiveReviews, trainingNegativeReviews)
# trainedNBClassifier, trainingFeatures = getTrainedNaiveBayesClassifier(extract_features,trainingData)

# print len(trainingPositiveReviews) # 5000
# print len(trainingNegativeReviews) # 5000
# print len(vocabulary) # 28492
# print len(trainingData) # 10000
# print len(trainingFeatures) #10000



# f = open('twitter_classifier.pickle', 'wb')
# pickle.dump(trainedNBClassifier, f)
# f.close()
#
# vocabulary_file = open('vocabulary.pickle', 'wb')
# pickle.dump(vocabulary, vocabulary_file)
# vocabulary_file.close()

# with open('./polaritydata/neg.txt','r') as f:
#     testNegativeReviews = f.readlines()
#
# with open('./polaritydata/pos.txt','r') as f:
#     testPositiveReviews = f.readlines()

def naiveBayesSentimentCalculator(review):
  problemInstance = review.split()
  problemFeatures = extract_features(problemInstance)
  return trainedNBClassifier.classify(problemFeatures)

def getTestReviewSentiments(naiveBayesSentimentCalculator):
  testNegResults = [naiveBayesSentimentCalculator(review) for review in testNegativeReviews]
  testPosResults = [naiveBayesSentimentCalculator(review) for review in testPositiveReviews]
  labelToNum = {'positive':1,'negative':-1}
  numericNegResults = [labelToNum[x] for x in testNegResults]
  numericPosResults = [labelToNum[x] for x in testPosResults]
  return {'results-on-positive':numericPosResults, 'results-on-negative':numericNegResults}


def runDiagnostics(reviewResult):
  positiveReviewsResult = reviewResult['results-on-positive']
  negativeReviewsResult = reviewResult['results-on-negative']
  numTruePositive = sum(x > 0 for x in positiveReviewsResult)
  numTrueNegative = sum(x < 0 for x in negativeReviewsResult)
  pctTruePositive = float(numTruePositive)/len(positiveReviewsResult)
  pctTrueNegative = float(numTrueNegative)/len(negativeReviewsResult)
  totalAccurate = numTruePositive + numTrueNegative
  total = len(positiveReviewsResult) + len(negativeReviewsResult)
  print "Accuracy on positive reviews = " +"%.2f" % (pctTruePositive*100) + "%"
  print "Accurance on negative reviews = " +"%.2f" % (pctTrueNegative*100) + "%"
  print "Overall accuracy = " + "%.2f" % (totalAccurate*100/total) + "%"

# reviewResult = getTestReviewSentiments(naiveBayesSentimentCalculator)
# runDiagnostics(reviewResult)
