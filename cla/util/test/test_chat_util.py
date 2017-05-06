# coding=utf-8
from cla.util import chat_util


def test_process_qq_history():
    test_file_path = "res/test/qq.txt"
    result_path = chat_util.process_qq_history(test_file_path)

    import os
    assert os.path.isfile(result_path)
    assert os.path.getsize(result_path) > 0
