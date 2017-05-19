# coding=utf-8
def process_qq_history(path, skip_system=True, encoding="utf-8", strip=None, output_path=None):
    """
    Process QQ chat history export text file to sentences.
    
    :param path: Path to QQ history txt file.
    :param skip_system: Skip system message if set.
    :param encoding: Encoding of the txt file.
    :param strip: Chars to be stripped out.
    :param output_path: Path to save output.
    :return: Processed result path.
    """
    import re

    # Generate result filename.
    if not output_path:
        import os
        _, filename = os.path.split(path)
        result_path = "sentences_in_" + filename
    else:
        result_path = output_path

    # Open files.
    with open(path, 'r') as the_file, open(result_path, 'w') as result_file:

        # Skip first 7 lines. This will skip until the line before the first system message.
        skip = 7

        # 0 stands for the empty line before each message.
        # 1 stands for the speaker information line.
        # 2 stands for the actual message sent.
        line_category = 0

        # Iterate through the file.
        for line in the_file:

            # Skip lines.
            if skip > 0:
                skip -= 1
                continue

            content = line.decode(encoding=encoding)
            if content == u"\r\n":
                # Reset line category to 0.
                line_category = 0
                continue
            else:
                line_category += 1

            # Skip system messages.
            if line_category == 1:
                if skip_system and "(10000)" in content:
                    skip += 1
                continue

            else:
                # Strip unnecessary characters.
                content = re.sub(r'\[.+\]', '', content).strip(strip)
                # Write result if not empty.
                if content:
                    result_file.write(content.encode(encoding=encoding) + "\n")

    return result_path


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

    if not output_path:
        import os
        _, filename = os.path.split(path)
        result_path = "words_in_" + filename
    else:
        result_path = output_path

    with open(result_path, 'w') as result_file:
        for words in CutDocument(path, cut=False, skip_prefixes=skip_prefixes, strip=strip):
            result_line = " ".join(words)
            result_file.write(result_line.encode(encoding=encoding) + "\n")
    return result_path


def cut_words(line, cleanup=False):
    """
    Cut a sentence in unicode.
    
    :param line: Unicode sentence.
    :param cleanup: Delete meaningless words, like "这个", if true. 
    :return: A list of words.
    """

    import jieba
    from unicodedata import category

    # Delete punctuation words.
    content = ''.join(ch for ch in line if category(ch)[0] != 'P')

    if cleanup:
        import jieba.posseg as pseg
        words = []
        # POS tagging.
        terms = pseg.cut(content)
        for term, tag in terms:
            if (
                tag.startswith(u"c") or tag.startswith(u"e") or
                tag.startswith(u"r") or tag.startswith(u"p") or
                tag.startswith(u"u") or tag.startswith(u"w") or
                tag.startswith(u"y") or tag.startswith(u"v") or
                tag.startswith(u"m") or tag.startswith(u"q") or
                tag.startswith(u"d")
            ):
                continue
            words.append(term)
        return words
    else:
        # Word segmentation.
        terms = jieba.cut(content)
        return map(unicode, terms)


class CutDocument(object):
    """
    Iterate though document, generates a list of cut words per-line.
    """

    def __init__(self, document, cut=True, encoding="utf-8", skip_prefixes=None, strip=None, cleanup=False):
        """
        Constructor.
        
        :param document: Path to document that contains one sentences per-line, or a list of sentences.
        :param cut: Is the document already cut.
        :param encoding: Encoding of the document.
        :param skip_prefixes: Lines start with this prefix will be skipped.
        :param strip: Chars to be stripped out.
        :param cleanup: Delete meaningless words, like "这个", if true. 
        """

        self.document = document
        self.cut = cut
        self.encoding = encoding
        self.skip_prefixes = skip_prefixes
        self.strip = strip
        self.cleanup = cleanup

    def __iter__(self):
        if isinstance(self.document, list):
            the_document = self.document
        else:
            the_document = open(self.document, 'r')

        with the_document:
            for line in the_document:
                if self.cut:
                    yield line.decode(encoding=self.encoding).split(" ")
                else:
                    # Decode and strip.
                    content = line.decode(encoding=self.encoding).strip(self.strip)

                    # Skip empty lines and lines with skip prefix.
                    if not content:
                        continue
                    if self.skip_prefixes:
                        skip = False
                        for item in self.skip_prefixes:
                            if content.startswith(item.decode(self.encoding)):
                                skip = True
                        if skip:
                            continue

                    yield cut_words(content, cleanup=self.cleanup)
