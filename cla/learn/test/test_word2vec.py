# coding=utf-8
from cla.learn.word2vec import VectorModel
import pytest


@pytest.fixture(scope="module")
def setup_model():
    model = VectorModel(source_corpus_path="res/test/words.txt")
    return model


def test_vector_model(setup_model):
    similar_words = setup_model.model.most_similar(u"美国")
    vector = setup_model.to_vector([u"美国", u"网民", u"纷纷", u"谴责", u"美联航", u"暴力", u"逐客", u"事件"])

    print similar_words
    assert similar_words.__sizeof__() > 0
    print vector
    assert vector.__sizeof__() > 0


def test_save_vector_model(setup_model):
    setup_model.save("res/test/model.bin")
    loaded_model = VectorModel("res/test/model.bin")
    assert loaded_model.model is not None
