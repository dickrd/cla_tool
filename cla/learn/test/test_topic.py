from cla.learn.topic import TopicModel
from cla.util.util import CutDocument


def test_topic():
    path = "cla/res/test/sentences.txt"
    out = "cla/res/test/topics.txt"
    model = TopicModel(path, cut=False, num_topics=3)
    all_topics = model.all_topics()
    print all_topics
    assert all_topics.__len__() == 3

    document = CutDocument(path, cut=False)
    with open(out, 'w') as output:
        for words in document:
            model.identify_topic(words)
