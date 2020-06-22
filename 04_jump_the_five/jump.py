#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 22-06-2020
Purpose: Encode and decode a number by jumping the 5
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Encode and decode a number by jumping the 5",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()

jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
          '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    output = ''
    for char in text:
       if char in jumper:
           output = output + jumper[char]
       else:
           output = output + char
    print(output)

 #   for char in text:
 #       print(jumper.get(char, char), end='')
 #   print() #newline

 #   print(text.translate(str.maketrans(jumper)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
