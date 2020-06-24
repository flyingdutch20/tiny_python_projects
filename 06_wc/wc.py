#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 24/06/2020
Purpose: Count the words
"""

import argparse
import sys


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
    total_lines = 0
    total_words = 0
    total_bytes = 0
    for fh in args.files:
        my_words = 0
        my_lines = 0
        for line in fh:
            my_lines += 1
            my_words = my_words + len(line.split())
        total_lines = total_lines + my_lines
        total_words = total_words + my_words
        total_bytes = total_bytes + bytes(fh)
        print('{########} {########} {########} {}'.format(my_lines, my_words), bytes(fh), fh.name())
    if len(fh) > 1:
        print('{########} {########} {########} total'.format(total_lines, total_words), total_bytes)



    print(file_list)

# --------------------------------------------------
if __name__ == '__main__':
    main()
