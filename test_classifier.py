import pytest
from twitter_classifier import extract_features, getVocabulary, getTrainingData, getTrainedNaiveBayesClassifier


def multiply(a, b):
    return a * b

def test_numbers_3_4():
    assert multiply(3,4) == 12


def test_extract_features(): # can't take vocabulary as parameter anymore
    assert set(extract_features("this is a test").values()) == set([False, True])

def test_getVocabulary():
    assert getVocabulary(["amazing", "great"],["terrible","worst"]) == ["amazing", "worst", "great", "terrible"]

def test_getTrainingData():
    assert getTrainingData(["amazing", "great"],["terrible","worst"]) == [(["terrible"],'negative'),(["worst"],'negative'),(['amazing'],'positive'),(['great'], 'positive')]

# def test_getTrainedNaiveBayesClassifier():
#     # assert getTrainedNaiveBayesClassifier()
#     pass
