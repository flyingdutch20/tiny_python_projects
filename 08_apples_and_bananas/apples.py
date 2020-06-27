#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 27/06/2020
Purpose: Replace vowels
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Replace the vowels in a piece of text by a different vowel",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
#                        choices= ['a', 'e', 'i', 'o', 'u'],
                        choices= list('aeiou'),
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    text = open(args.text).read().rstrip() if os.path.isfile(args.text) else args.text
    vowel = args.vowel
#    table = str.maketrans({'a': vowel, 'e': vowel, 'i': vowel, 'o': vowel, 'u': vowel,
#                           'A': vowel.upper(), 'E': vowel.upper(), 'I': vowel.upper(),
#                           'O': vowel.upper(), 'U': vowel.upper()})
#    table = str.maketrans('aeiouAEIOU', vowel * 5 + vowel.upper() * 5)
#    output = text.translate(table)
#    print(output)

# using map() and lambda
    output = map(
        lambda c: vowel if c in 'aeiou' else vowel.upper()
        if c in 'AEIOU' else c, text)
    print(''.join(output))

# using re
    print(re.sub('[aeiou]', vowel, re.sub('[AEIOU]', vowel.upper(), text)))



# --------------------------------------------------
if __name__ == '__main__':
    main()
