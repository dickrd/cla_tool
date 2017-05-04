# coding=utf-8
def read_as_set(path, encoding="utf-8", skip=0, skip_prefix=None, strip=None):
    """
    Read a text file and form a set using each line in it.
    
    :param path: Path to the file.
    :param encoding: Encoding fo the text.
    :param skip: Line count to skip.
    :param skip_prefix: Skip lines with this prefix.
    :param strip: Chars to be stripped out.
    :return: A set in which is the non-empty lines of the file.
    """
    result_set = set()
    skips = skip
    with open(path, 'r') as the_file:
        for line in the_file:
            if skips > 0:
                skips -= 1
                continue

            content = line.decode(encoding=encoding).strip(strip)
            if not content:
                continue
            if skip_prefix is not None and content.startswith(prefix=skip_prefix):
                continue

            result_set.add(content)
    return result_set


def cut_words_in(path, encoding="utf-8", strip=None):
    """
    Cut each line in the file into words and stores it in the same directory with a "cut_" prefix in file name.
    
    :param path: Path to the file to cut.
    :param encoding: Encoding fo the file.
    :param strip: Chars to be stripped out.
    :return: Path to the result file.
    """
    import jieba
    import os
    directory, filename = os.path.split(path)
    result_path = directory + "/words_in_" + filename
    with open(path, 'r') as the_file, open(result_path, 'w') as result_file:
        for line in the_file:
            content = line.decode(encoding=encoding).strip(strip)
            if not content:
                continue

            result_line = ""
            terms = jieba.cut(content)
            for term in terms:
                result_line += term + " "
            result_file.write(result_line.encode(encoding=encoding).strip() + "\n")
    return result_path
