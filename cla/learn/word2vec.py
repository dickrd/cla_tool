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
        else:
            self.model = Doc2Vec(min_count=10, window=10, size=200, sample=1e-4, negative=5, workers=8)

        if source_corpus_path:
            self.train(source_corpus_path)

    def train(self, source_corpus_path, update=False):
        """
        Train an uninitialized model using corpus.
        Each line in the corpus should be words of a sentence separated by space.
        
        :param source_corpus_path: Path to corpus.
        :param update: Update vocab.
        :return: Nothing.
        """
        documents = TaggedLineDocument(source_corpus_path)
        self.model.build_vocab(documents, update=update)
        self.model.train(documents, total_examples=self.model.corpus_count, epochs=self.model.iter)

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

    def similar_documents(self, vector):
        """
        Find documents similar to the given vector.
        
        :param vector: Vector to find similar for.
        :return: A list of similar document ids.
        """
        if not self.model:
            raise RuntimeError("model not initialized.")
        return self.model.docvecs.most_similar([vector])

    def predict(self, words):
        """
        Predict output word for a list of context words.
        
        :param words: A list of context words.
        :return: Predictions.
        """
        if not self.model:
            raise RuntimeError("model not initialized.")
        return self.model.predict_output_word(words)
