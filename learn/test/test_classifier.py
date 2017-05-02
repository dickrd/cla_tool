import pytest

from learn.classifier import TraditionalClassifier


@pytest.fixture(scope="module")
def setup_classifier():
    classifier = TraditionalClassifier(vector_model_path="learn/test/model.bin", training_data_path="")
    return classifier


def test_traditional_classifier(setup_classifier):
    result = setup_classifier.classify([["", "", ""], ["", ""]])
    print result
    assert result.__sizeof__() > 0
    assert result[0] > 0
    assert result[1] < 0


def test_traditional_classifier_accuracy(setup_classifier):
    result = setup_classifier.test_with(test_data_path="")
    print result
    assert result > 0.5
