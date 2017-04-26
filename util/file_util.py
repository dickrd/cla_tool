# coding=utf-8
def read_as_set(path, encoding="utf-8", skip=0, skip_prefix=None, strip=None):
    result_set = set()
    skips = skip
    with open(path, 'r') as the_file:
        lines = the_file.readlines()
        for line in lines:
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
    import jieba
    import os
    directory, filename = os.path.split(path)
    result_path = directory + "/cut_" + filename
    with open(path, 'r') as the_file, open(result_path, 'w') as result_file:
        lines = the_file.readlines()
        for line in lines:
            content = line.decode(encoding=encoding).strip(strip)
            if not content:
                continue

            result_line = ""
            terms = jieba.cut(content)
            for term in terms:
                result_line += term + " "
            result_file.write(result_line.encode(encoding=encoding).strip() + "\n")
    return result_path
