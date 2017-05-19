from gensim.corpora import Dictionary
from gensim.models import LdaModel

from cla.util.util import CutDocument


class TopicModel(object):

    def __init__(self, documents, cut=True, num_topics=10):
        self.document = CutDocument(documents, cut)
        self.dictionary = Dictionary(self.document)
        self.model = LdaModel(BowCorpus(self.document, self.dictionary),
                              id2word=self.dictionary,
                              num_topics=num_topics)

    def all_topics(self):
        return self.model.show_topics(self.model.num_topics)

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
