#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 19/06/2020
Purpose: Shout what you can see from the Crow's nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='Enter the subject that you can see from the crow\'s nest')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = "an" if word[0].lower() in "aeiou" else "a"

    print("Ahoy, Captain, {} {} off the larboard bow!".format(article, word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
