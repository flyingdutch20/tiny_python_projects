#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 25 June 2020
Purpose: Return a name and a ghastly way to end
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Return a name and a ghastly way to end",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letters',
                        metavar='str',
                        nargs='+',
                        help='One or more letters')

    parser.add_argument('-f',
                        '--file',
                        help='A file with the text to parse',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='.\gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    fh = args.file
    lookup = {}
    for line in fh:
        if len(line.strip()) > 0:
            lookup[line[0].upper()] = line.strip()

    for letter in args.letters:
        print(lookup.get(letter.upper(), 'Sorry, no potato'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
