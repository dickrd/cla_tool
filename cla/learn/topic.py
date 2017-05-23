class TopicModel(object):

    def __init__(self, documents, cut=True, num_topics=10, min_length=1):
        from cla.util.util import CutDocument
        from gensim.corpora import Dictionary
        from gensim.models import LdaModel

        self.document = CutDocument(documents, cut, cleanup=True, min_length=min_length)
        self.dictionary = Dictionary(self.document)
        self.model = LdaModel(BowCorpus(self.document, self.dictionary),
                              id2word=self.dictionary,
                              num_topics=num_topics)

    def topic_words(self, topic_id, limit=10):
        return self.model.show_topic(topicid=topic_id, topn=limit)

    def identify_topic(self, words):
        return self.model.get_document_topics(self.dictionary.doc2bow(words))


class BowCorpus(object):
    """
    Iterate through cut corpus, generates a bow per-line.
    """

    def __init__(self, corpus, dictionary, encoding="utf-8"):
        """
        Constructor.
        
        :param corpus: CutDocument.
        :param dictionary: Dictionary to generate bow.
        :param encoding: Encoding of the sentences.
        """

        self.corpus = corpus
        self.dictionary = dictionary
        self.encoding = encoding

    def __iter__(self):
        for words in self.corpus:
            yield self.dictionary.doc2bow(words)


class TopicClustering(object):

    def __init__(self, vector_model_path, document_path, cut=True, num_topics=8, min_length=1):
        from cla.learn.word2vec import VectorModel
        from sklearn.cluster import KMeans
        from cla.util.util import CutDocument
        import numpy as np

        self.doc2vec = VectorModel(source_file_path=vector_model_path)

        vectors = []
        for words in CutDocument(document_path, cut, cleanup=True, min_length=min_length):
            vectors.append(self.doc2vec.to_vector(words))
        self.clustering = KMeans(n_clusters=num_topics)
        self.clustering.fit(np.asarray(vectors))

    def cluster(self, words):
        return self.clustering.predict([self.doc2vec.to_vector(words)])
