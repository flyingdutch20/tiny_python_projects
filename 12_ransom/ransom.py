#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 05 Aug 2020
Purpose: Randomly capitalising a string
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Randomly capitalising a string",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------

def choose(char):
    return char.upper() if random.choice([False, True]) else char.lower()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

#   nice simple solution
#    new_text = ''
#    for char in args.text:
#        new_text += choose(char)
#    print(new_text)

#   list comprehension
#    print(''.join([choose(char) for char in args.text]))

#   map
    print(''.join(map(choose, args.text)))


# --------------------------------------------------
# --------------------------------------------------
def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)

# --------------------------------------------------
if __name__ == '__main__':
    main()
