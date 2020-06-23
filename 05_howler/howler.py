#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 23/06/2020
Purpose: Howl the input text
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howl the input text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
#    outfile = args.outfile
#    text = args.input

    text = open(args.input).read().rstrip() if os.path.isfile(args.input) else args.input

#   if os.path.isfile(text):
#       text = open(text).read().rstrip()
#   text = text.upper()

#    if outfile:
#        out_fh = open(outfile, 'wt')
#        print(text, file=out_fh)
#        out_fh.close()
#    else:
#        print(text)

    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    print(text.upper(), file=out_fh)
    out_fh.close()





# --------------------------------------------------
if __name__ == '__main__':
    main()
