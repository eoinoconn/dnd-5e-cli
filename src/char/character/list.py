"""List characters module."""
import argparse
import logging
import json

from char.character.utils import get_char_save_files, CHAR_SAVE_PATH


def main(args: argparse.Namespace):
    """List characters."""
    logging.debug('List characters.')
    print('List characters.')

    char_files = get_char_save_files(CHAR_SAVE_PATH)
    if not char_files:
        print("No characters found.")
        return

    if args.verbose:
        print('Verbose output.')
        print(f"{'name':30}{'Level':<6}{'race':12}{'class':12}")

    for json_file in char_files:
        # open json file
        with open(json_file, 'r') as f:
            # load json file
            char_json = json.load(f)
            if not args.verbose:
                # print character name
                print(char_json['name'])
            else:
                print(
                    f"{char_json['name']:30}{char_json['level']:<6}" +
                    f"{char_json['race']:12}{char_json['cls']:12}")


def configure_parser_list(sub_parsers: argparse._SubParsersAction):
    """Configure the list sub-parser."""
    parser_list = sub_parsers.add_parser(
        'list',
        help='List characters.', #TODO: Fill this in
    )
    parser_list.add_argument(
        '-v', '--verbose', action='store_true', help='Verbose output.')
    parser_list.set_defaults(func=main)
