# coding=utf-8
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedLineDocument


class VectorModel(object):

    def __init__(self, source_file_path=None, source_corpus_path=None):
        if source_file_path:
            self.model = Doc2Vec.load(source_file_path)
        elif source_corpus_path:
            self.train(source_corpus_path)

    def train(self, source_corpus_path):
        documents = TaggedLineDocument(source_corpus_path)
        self.model = Doc2Vec(documents=documents, min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)

    def save(self, path):
        self.model.save(path)
