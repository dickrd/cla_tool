# coding=utf-8
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedLineDocument


class VectorModel(object):
    """Simple word to vectors model using doc2vec."""

    def __init__(self, source_file_path=None, source_corpus_path=None):
        """
        Initialize the model. If nothing is provided, the model is left uninitialized.
        
        :param source_file_path: Path to previous saved model.
        :param source_corpus_path: Path to corpus that can train a new model.
        """
        if source_file_path:
            self.model = Doc2Vec.load(source_file_path)
        elif source_corpus_path:
            self.train(source_corpus_path)

    def train(self, source_corpus_path):
        """
        Train an uninitialized model using corpus.
        Each line in the corpus should be words of a sentence separated by space.
        
        :param source_corpus_path: Path to corpus.
        :return: Nothing.
        """
        documents = TaggedLineDocument(source_corpus_path)
        self.model = Doc2Vec(documents=documents, min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)

    def save(self, path):
        self.model.save(path)

    def to_vector(self, words_of_sentence):
        """
        Translate a list of words into a vector.
        
        :param words_of_sentence: A list of words of a sentence.
        :return: The vector representation of the sentence.
        """
        if not self.model:
            raise RuntimeError("model not initialized.")
        return self.model.infer_vector(words_of_sentence)
