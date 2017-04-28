from sklearn.linear_model import LogisticRegression

from learn.word2vec import VectorModel


class TraditionalClassifier(object):
    """Classifier using traditional machine learning algorithm rather than deep learning."""

    def __init__(self, vector_model_path, training_data_path=None):
        """
        Build the classifier if training data is present.
        
        :param vector_model_path: Path to vector model.
        :param training_data_path: Path to training data.
        """
        self.classifier = LogisticRegression()
        self.vector_model = VectorModel(source_file_path=vector_model_path)

        if training_data_path:
            self.train(training_data_path)

    def train(self, training_data_path):
        training_label, training_data = self.read_formatted_data(training_data_path)
        self.classifier.fit(training_data, training_label)

    def classify(self, sentences):
        """
        Classifying a list of sentences. Each sentence is words in array-like format.
        
        :param sentences: The sentences to classify.
        :return: Classified label.
        """
        vectors = []
        for sentence in sentences:
            vectors.append(self.vector_model.to_vector(sentence))

        return self.classifier.predict(vectors)

    def test_with(self, test_data_path):
        """
        Calculating overall accuracy in predicting data provided.
        
        :param test_data_path: Path to the test data.
        :return: Overall accuracy.
        """
        test_label, test_data = self.read_formatted_data(test_data_path)
        return self.classifier.score(test_data, test_label)

    def read_formatted_data(self, path):
        """
        Read data in the format that each line are words of a sentence with a label separated by a space. 
        The label should be at first and the rest of the line should be words of the sentence.
        
        :param path: Path to the data.
        :return: A list of labels and a list of sentences in order.
        """
        label = []
        data = []
        with open(path, 'r') as the_file:
            lines = the_file.readlines()
            for line in lines:
                splits = line.split(" ")
                data.append(self.vector_model.to_vector(splits[1:]))
                label.append(splits[0])

        return label, data
