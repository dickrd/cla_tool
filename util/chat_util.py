# coding=utf-8
def process_qq_history(path, skip_system=True, encoding="utf-8", strip=None, output_path=None):
    import os
    import re

    # Generate result filename.
    if not output_path:
        directory, filename = os.path.split(path)
        result_path = directory + "/sentences_in_" + filename
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
            if line_category is 1:
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
