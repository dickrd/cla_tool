# coding=utf-8
def read_as_set(path, encoding="utf-8", skip=0, skip_prefixes=None, strip=None):
    """
    Read a text file and form a set using each line in it.
    
    :param path: Path to the file.
    :param encoding: Encoding fo the text.
    :param skip: Line count to skip.
    :param skip_prefixes: Skip lines with this prefix.
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
            if skip_prefixes:
                skip = False
                for item in skip_prefixes:
                    if content.startswith(item.decode(encoding)):
                        skip = True
                if skip:
                    continue

            result_set.add(content)
    return result_set


def cut_words_in(path, encoding="utf-8", skip_prefixes=None, strip=None, output_path=None):
    """
    Cut each line in the file into words and stores it in the same directory with a "cut_" prefix in file name.
    
    :param path: Path to the file to cut.
    :param encoding: Encoding fo the file.
    :param skip_prefixes: Lines start with this prefix will be skipped.
    :param strip: Chars to be stripped out.
    :param output_path: Path to save output.
    :return: Path to the result file.
    """
    import jieba
    from unicodedata import category

    if not output_path:
        import os
        _, filename = os.path.split(path)
        result_path = "words_in_" + filename
    else:
        result_path = output_path

    with open(path, 'r') as the_file, open(result_path, 'w') as result_file:
        for line in the_file:
            content = line.decode(encoding=encoding).strip(strip)
            if not content:
                continue
            if skip_prefixes:
                skip = False
                for item in skip_prefixes:
                    if content.startswith(item.decode(encoding)):
                        skip = True
                if skip:
                    continue

            content = ''.join(ch for ch in content if category(ch)[0] != 'P')
            terms = jieba.cut(content)
            result_line = " ".join(map(unicode, terms))
            result_file.write(result_line.encode(encoding=encoding) + "\n")
    return result_path
