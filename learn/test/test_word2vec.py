# coding=utf-8
from learn.word2vec import VectorModel


def test_vector_model():
    model = VectorModel(source_corpus_path="util/test/cut_test.txt")
    similar_words = model.model.most_similar(u"美国")
    vector = model.to_vector([u"美国", u"网民", u"纷纷", u"谴责", u"美联航", u"暴力", u"逐客", u"事件"])

    print similar_words
    assert similar_words.__sizeof__() > 0
    print vector
    assert vector.__sizeof__() > 0
