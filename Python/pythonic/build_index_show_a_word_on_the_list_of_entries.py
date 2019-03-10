"""
Build a index that show number of mentions of each words.
"""

import sys
import re

WORD_RE = re.compile('\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as file:
    for line_no, line in enumerate(file, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # Pythonic style
            index.setdefault(word, []).append(location)
            # or
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences

for word in sorted(index, key=str.upper):
    print(word, index[word])
