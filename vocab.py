# coding: utf-8
# Copyright (C) 2017 FireEye, Inc. All Rights Reserved.
#
# Reads source files (*.{c,h,cpp,hpp,txt}) as code page 1251
# Writes a prioritized vocabularly list in UTF-8.
#
# For details, see README.md

import os
import re
import codecs
import string
import fnmatch
import argparse
import operator
from collections import defaultdict

def parse(f, word_frequencies, encoding='cp1251'):
    with codecs.open(f, 'r', encoding) as infile:
        for line in infile.readlines():
            # Omit ASCII characters (between space (0x20) and tilde (0x7e))
            words = re.split('[ -~]+', line)
            for word in words:
                word = word.strip(' \t\r\n\0')
                if len(word):
                    word_frequencies[word] += 1

def parse_args():
    desc = 'Vocabulary scraper'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('outfile', help='Output file')
    parser.add_argument('--startdir', default='.', help='Directory to recurse')
    parser.add_argument('--ienc', default='cp1251', help='Input encoding')
    parser.add_argument('--oenc', default='utf-8', help='Output encoding')
    return parser.parse_args()

def main():
    args = parse_args()

    word_frequencies = defaultdict(int)

    files = []
    masks = ['*.c', '*.h', '*.cpp', '*.hpp', '*.txt', '*.cs']
    for root, dirnames, filenames in os.walk(args.startdir):
        for mask in masks:
            for filename in fnmatch.filter(filenames, mask):
                files.append(os.path.join(root, filename))

    for file in files:
        try:
            parse(file, word_frequencies, args.ienc)
        except UnicodeDecodeError:
            pass

    sorted_words = sorted(word_frequencies.items(), key=operator.itemgetter(1))
    sorted_words.reverse()
    with codecs.open(args.outfile, 'w', args.oenc) as outfile:
        for s, n in sorted_words:
            outfile.write(str(n) + ': ' + s + '\r\n')

if __name__ == '__main__':
    main()
