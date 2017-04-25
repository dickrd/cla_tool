# coding=utf-8
from util import file_util


def test_read_strength():
    strength_path = "res/程度级别词语.txt"
    most = file_util.read_as_set(strength_path, encoding="gbk", skip=3)
    ish = file_util.read_as_set(strength_path, encoding="gbk", skip=157)

    assert most.__sizeof__() > 0
    assert ish.__sizeof__() > 0
    assert most.__contains__(u"百分之百")
    assert ish.__contains__(u"点点滴滴")
