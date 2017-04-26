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


def test_cut_words_in():
    test_file_path = "util/test/test.txt"
    result_path = file_util.cut_words_in(test_file_path)
    with open(result_path, 'r') as result_file:
        first_line = result_file.readline()
        assert first_line is not None
        assert first_line.split(" ").__sizeof__() > 0
