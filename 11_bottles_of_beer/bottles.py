#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 4 Aug 2020
Purpose: Sing the Bottles of Beer song with countdown
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Sing the Bottles of Beer song with countdown",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error((f'--num "{args.num}" must be greater than 0'))

    return args

# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    last = (bottle == 1)
    plural = 's' if not last else ''
    last_line_plural = 's' if bottle > 2 else ''
    last_line = '{} bottle{} of beer on the wall!\n'.format(bottle - 1, last_line_plural)
    if last:
        last_line = 'No more bottles of beer on the wall!'

    return '\n'.join([
        '{} bottle{} of beer on the wall,'.format(bottle, plural),
        '{} bottle{} of beer,'.format(bottle, plural),
        'Take one down, pass it around,',
        last_line
    ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

#    print([verse(n) for n in range(args.num, 0, -1)])
    print(map(verse, range(args.num, 0, -1)))

# --------------------------------------------------
# --------------------------------------------------
def test_verse():
    """Test the verse() function"""

    last_verse = verse(1)
    print(last_verse)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,',
        '1 bottle of beer.',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    print(two_bottles)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,',
        '2 bottles of beer.',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
