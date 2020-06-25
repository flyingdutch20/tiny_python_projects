#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 24/06/2020
Purpose: Count the words
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Count the words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('r'),
                        default=[sys.stdin],
                        help = 'Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_lines, total_words, total_bytes = 0, 0, 0
    for fh in args.files:
        my_words, my_lines, my_bytes = 0, 0, 0
        for line in fh:
            my_lines += 1
            my_words += len(line.split())
            my_bytes += len(line)
        total_lines += my_lines
        total_words += my_words
        total_bytes += my_bytes
        print('{:8}{:8}{:8} {}'.format(my_lines, my_words, my_bytes, fh.name))
    if len(args.files) > 1:
        print('{:8}{:8}{:8} total'.format(total_lines, total_words, total_bytes))


# --------------------------------------------------
if __name__ == '__main__':
    main()
