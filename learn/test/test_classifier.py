# coding=utf-8
import pytest

from learn.classifier import TraditionalClassifier


@pytest.fixture(scope="module")
def setup_classifier():
    classifier = TraditionalClassifier(vector_model_path="res/test/model.bin",
                                       training_data_path="res/test/labeled_train.txt")
    return classifier


def test_traditional_classifier(setup_classifier):
    result = setup_classifier.classify([[u"这样", u"的", u"好事", u"应该", u"多", u"搞"],
                                        [u"小偷", u"太", u"坏"]])
    print result
    assert result.__sizeof__() > 0
    assert result[0] > 0
    assert result[1] < 0


def test_traditional_classifier_accuracy(setup_classifier):
    result = setup_classifier.test_with(test_data_path="res/test/labeled_test.txt")
    print result
    assert result > 0.5
