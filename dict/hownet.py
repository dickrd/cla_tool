# coding=utf-8
from util import file_util
import thulac


class Hownet(object):
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

    def score(self, sentence):
        score = 0
        nlp = thulac.thulac(seg_only=True)
        terms = nlp.cut(sentence)

        sign = 1
        count = 0
        for term in terms:
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
        return score / count
