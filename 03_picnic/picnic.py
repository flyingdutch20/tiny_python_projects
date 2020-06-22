#!/usr/bin/env python3
"""
Author : Ted <ted@bracht.uk>
Date   : 20/06/2020
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sort = args.sorted
    items = args.items

    if sort:
        items.sort()

    items_output = items[0]
    if len(items) == 2:
        items_output = items_output + ' and ' + items[-1]
    elif len(items) > 2:
        for item in items[1:-1]:
            items_output = items_output + ', ' + item
        items_output = items_output + ', and ' + items[-1]

    num = len(items)
    items_output = ""
    if num == 1:
        items_output = items[0]
    elif num == 2:
        items_output = " and ".join(items)
    else:
        items_output = ", ".join(items[0:-1]) + ", and " + items[-1]

    print("You are bringing {}.".format(items_output))



# --------------------------------------------------
if __name__ == '__main__':
    main()
