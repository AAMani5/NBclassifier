import pytest
from classifier import extract_features, getVocabulary, getTrainingData, getTrainedNaiveBayesClassifier


def multiply(a, b):
    return a * b

def test_numbers_3_4():
    assert multiply(3,4) == 12


# def test_extract_features():
#     # assert extract_features("this is a test") ==
#     pass
#
# def test_getVocabulary():
#     # assert getVocabulary()
#     pass
#
# def test_getTrainingData():
#     # assert getTrainingData()
#     pass
#
# def test_getTrainedNaiveBayesClassifier():
#     # assert getTrainedNaiveBayesClassifier()
#     pass
