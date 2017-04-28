from learn.classifier import TraditionalClassifier

classifier = TraditionalClassifier(vector_model_path="", training_data_path="")


def test_traditional_classifier():
    result = classifier.classify([["", "", ""], ["", ""]])
    print result
    assert result.__sizeof__() > 0
    assert result[0] > 0
    assert result[1] < 0


def test_traditional_classifier_accuracy():
    result = classifier.test_with(test_data_path="")
    print result
    assert result > 0.5
