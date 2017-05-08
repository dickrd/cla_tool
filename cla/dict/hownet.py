# coding=utf-8
from cla.util import file_util


class Hownet(object):
    """Class for reading hownet vocabulary and score the sentiment of a sentence based on it."""

    def __init__(self,
                 positive_emotions_path,
                 positive_judgement_path,
                 negative_emotions_path,
                 negative_judgement_path,
                 strength_path):
        self.positive_emotions = file_util.read_as_set(positive_emotions_path, encoding="gbk", skip=1)
        self.positive_judgement = file_util.read_as_set(positive_judgement_path, encoding="gbk", skip=1)
        self.negative_emotions = file_util.read_as_set(negative_emotions_path, encoding="gbk", skip=1)
        self.negative_judgement = file_util.read_as_set(negative_judgement_path, encoding="gbk", skip=1)
        self.strength_most = file_util.read_as_set(strength_path, encoding="gbk", skip=3)
        self.strength_very = file_util.read_as_set(strength_path, encoding="gbk", skip=74)
        self.strength_more = file_util.read_as_set(strength_path, encoding="gbk", skip=118)
        self.strength_ish = file_util.read_as_set(strength_path, encoding="gbk", skip=157)
        self.strength_week = file_util.read_as_set(strength_path, encoding="gbk", skip=188)
        self.strength_over = file_util.read_as_set(strength_path, encoding="gbk", skip=202)

    def score(self, words_of_sentence):
        """
        Score the sentiment of the sentence based on Hownet dictionary. Only supports Chinese.
        The sentence should already be cut.
        
        :param words_of_sentence: Words of a sentence to be scored.
        :return: Sentiment score. The higher the score is, the more positive the sentence.
        """
        score = 0.0

        sign = 1
        count = 1
        for term in words_of_sentence:
            count += 1
            if self.positive_emotions.__contains__(term):
                score += sign * 1.5
                sign = 1
                continue
            if self.positive_judgement.__contains__(term):
                score += sign * 1
                sign = 1
                continue
            if self.negative_emotions.__contains__(term):
                score -= sign * 1.5
                sign = 1
                continue
            if self.negative_judgement.__contains__(term):
                score -= sign * 1
                sign = 1
                continue
            if self.strength_most.__contains__(term):
                sign = 2
                continue
            if self.strength_very.__contains__(term):
                sign = 1.5
                continue
            if self.strength_more.__contains__(term):
                sign = 1
                continue
            if self.strength_ish.__contains__(term):
                sign = 0.5
                continue
            if self.strength_over.__contains__(term):
                sign = -0.5
                continue

            if term == u"不":
                sign = -sign
                continue

            count -= 1
        return score / count
