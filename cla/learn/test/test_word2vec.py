# coding=utf-8
from cla.learn.word2vec import VectorModel
import pytest


@pytest.fixture(scope="module")
def setup_model():
    model = VectorModel(source_corpus_path="cla/res/test/words.txt")
    return model


def test_vector_model(setup_model):
    vector = setup_model.to_vector([u"美国", u"网民", u"纷纷", u"谴责", u"美联航", u"暴力", u"逐客", u"事件"])
    similar_documents = setup_model.similar_documents(vector)

    print similar_documents
    assert similar_documents.__sizeof__() > 0
    print vector
    assert vector.__sizeof__() > 0


def test_save_vector_model(setup_model):
    setup_model.save("cla/res/test/model.bin")
    loaded_model = VectorModel("cla/res/test/model.bin")
    assert loaded_model.model is not None
