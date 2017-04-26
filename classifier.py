import nltk



positiveReviewsFileName = "./polaritydata/fin.pos"
negativeReviewsFileName = "./polaritydata/fin.neg"

with open(positiveReviewsFileName,'rb') as f:
    trainingPositiveReviews = f.readlines()

with open(negativeReviewsFileName,'rb') as f:
    trainingNegativeReviews = f.readlines()

# testTrainingSplitIndex = 2500

# testNegativeReviews = negativeReviews[testTrainingSplitIndex+1:]
# testPositiveReviews = positiveReviews[testTrainingSplitIndex+1:]
#
# trainingNegativeReviews = negativeReviews[:testTrainingSplitIndex]
# trainingPositiveReviews = positiveReviews[:testTrainingSplitIndex]



# def getTestReviewSentiments(naiveBayesSentimentCalculator):
#   testNegResults = [naiveBayesSentimentCalculator(review) for review in testNegativeReviews]
#   testPosResults = [naiveBayesSentimentCalculator(review) for review in testPositiveReviews]
#   labelToNum = {'positive':1,'negative':-1}
#   numericNegResults = [labelToNum[x] for x in testNegResults]
#   numericPosResults = [labelToNum[x] for x in testPosResults]
#   return {'results-on-positive':numericPosResults, 'results-on-negative':numericNegResults}
#
#
# def runDiagnostics(reviewResult):
#   positiveReviewsResult = reviewResult['results-on-positive']
#   negativeReviewsResult = reviewResult['results-on-negative']
#   numTruePositive = sum(x > 0 for x in positiveReviewsResult)
#   numTrueNegative = sum(x < 0 for x in negativeReviewsResult)
#   pctTruePositive = float(numTruePositive)/len(positiveReviewsResult)
#   pctTrueNegative = float(numTrueNegative)/len(negativeReviewsResult)
#   totalAccurate = numTruePositive + numTrueNegative
#   total = len(positiveReviewsResult) + len(negativeReviewsResult)
#   print "Accuracy on positive reviews = " +"%.2f" % (pctTruePositive*100) + "%"
#   print "Accurance on negative reviews = " +"%.2f" % (pctTrueNegative*100) + "%"
#   print "Overall accuracy = " + "%.2f" % (totalAccurate*100/total) + "%"
#


def getVocabulary():
  positiveWordList = [word for line in trainingPositiveReviews for word in line.split()]
  negativeWordList = [word for line in trainingNegativeReviews for word in line.split()]
  allWordList = [item for sublist in [positiveWordList,negativeWordList] for item in sublist]
  allWordSet = list(set(allWordList))
  vocabulary = allWordSet
  return vocabulary

def getTrainingData():
  negTaggedTrainingReviewList = [{'review':oneReview.split(),'label':'negative'} for oneReview in trainingNegativeReviews]
  posTaggedTrainingReviewList = [{'review':oneReview.split(),'label':'positive'} for oneReview in trainingPositiveReviews]
  fullTaggedTrainingData = [item for sublist in [negTaggedTrainingReviewList,posTaggedTrainingReviewList] for item in sublist]
  trainingData = [(review['review'],review['label']) for review in fullTaggedTrainingData]
  return trainingData




def extract_features(review):
  review_words=set(review)
  features={} # Dictionary
  for word in vocabulary: # Keys corresponding to the word in vocabulary
      features[word]=(word in review_words) # Values either true or false,
                            # Depending if the worst was present in the review
  return features


def getTrainedNaiveBayesClassifier(extract_features, trainingData):
  trainingFeatures=nltk.classify.apply_features(extract_features, trainingData)
  trainedNBClassifier=nltk.NaiveBayesClassifier.train(trainingFeatures) # Train the Classifier
  return trainedNBClassifier

vocabulary = getVocabulary()
trainingData = getTrainingData()
trainedNBClassifier = getTrainedNaiveBayesClassifier(extract_features,trainingData)
