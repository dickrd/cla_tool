# coding=utf-8
from cla.learn.topic import TopicModel, TopicClustering
from cla.util import util


def test_topic():
    path = "cla/res/test/sentences.txt"
    out = "cla/res/test/topics.txt"
    model = TopicModel(path, cut=False, num_topics=3)
    topic_count = model.model.num_topics
    assert topic_count == 3

    r = {}
    with open(path, 'r') as input_file:
        for line in input_file:
            document_topic, _ = model.identify_topic(util.cut_words(line.decode("utf-8")))[0]
            if document_topic not in r:
                r[document_topic] = []
            r[document_topic].append(line)

    with open(out, 'w') as output:
        for topic_id in r:
            topic_words = model.topic_words(topic_id, 10)
            topic = str(topic_id) + ": " + " ".join([x for x, _ in topic_words]).encode("utf-8")
            output.write("=====\n" + topic + "\n-----\n")
            for sentence in r[topic_id]:
                output.write(sentence)
            output.write("\n")


def test_clustering():
    path = "cla/res/test/sentences.txt"
    model = "cla/res/test/model.bin"
    model = TopicClustering(vector_model_path=model, document_path=path, cut=False)
    result = model.cluster([u"最", u"绝望", u"的", u"就是",
                            u"当", u"你", u"神", u"开局", u"两波",
                            u"蛮骑", u"直奔", u"你", u"而", u"来"])
    print result
    assert result[0] >= 0
