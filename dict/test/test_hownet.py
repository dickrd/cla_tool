# coding=utf-8
import pytest

from dict.hownet import Hownet


@pytest.fixture(scope="module")
def setup_hownet():
    hownet = Hownet(strength_path="res/程度级别词语.txt",
                    positive_emotions_path="res/正面情感词语.txt",
                    positive_judgement_path="res/正面评价词语.txt",
                    negative_emotions_path="res/负面情感词语.txt",
                    negative_judgement_path="res/负面评价词语.txt")
    return hownet


def test_score(setup_hownet):
    import jieba
    score1 = setup_hownet.score(jieba.cut("我非常喜欢这个电影！"))
    score2 = setup_hownet.score(jieba.cut("我觉得这个电影还不错。"))
    score3 = setup_hownet.score(jieba.cut("我不喜欢这个电影。"))
    score4 = setup_hownet.score(jieba.cut("这个电影十分令人讨厌！"))

    assert score1 > score2
    assert score2 > score3
    assert score3 > score4
