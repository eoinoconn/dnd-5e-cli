"""List characters module."""
import argparse
import logging
from typing import List
import json

from char.character.utils import get_char_save_files, CHAR_SAVE_PATH

def main(args: argparse.Namespace):
    """List characters."""
    logging.debug('List characters.')
    print('List characters.')

    if args.verbose:
        print('Verbose output.')
        print(f"{'name':30}{'Level':12}{'race':12}{'class':12}")

    for json_file in get_char_save_files(CHAR_SAVE_PATH):
        # open json file
        with open(json_file, 'r') as f:
            # load json file
            char_json = json.load(f)
            if not args.verbose:
                # print character name
                print(char_json['name'])
            else:
                print(f"{char_json['name']:30}{char_json['level']:12}{char_json['race']:12}{char_json['cls']:12}")




def configure_parser_list(sub_parsers: argparse._SubParsersAction):
    """Configure the list sub-parser."""
    parser_list = sub_parsers.add_parser(
        'list',
        help='List characters.',
    )
    parser_list.add_argument('-v', '--verbose', action='store_true', help='Verbose output.')
    parser_list.set_defaults(func=main)