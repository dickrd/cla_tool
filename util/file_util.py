# coding=utf-8
def read_as_set(path, encoding="utf-8", skip=0, skip_prefix=None, strip=None):
    result_set = set()
    skips = skip
    with open(path) as the_file:
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
