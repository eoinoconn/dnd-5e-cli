import argparse
from argparse import SUPPRESS
import logging

#from .. import __version__
from .character.create import configure_parser_create
from .character.list import configure_parser_list
from .character.utils import create_dir_structure
from .character.select import select_character

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def main():

    # establish configuration directory.
    create_dir_structure()

    parser = argparse.ArgumentParser(
        allow_abbrev=False,
        description='Command to create and manage your characters.',
    )

    parser.add_argument(
        '-V', '--version',
        action='version',
        # version= f"5e {__version__}", #TODO: fill in
        help="Show the 5e_cli version number and exit."
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help=SUPPRESS,
    )

    # if select is specified run the select command.
    parser.add_argument(
        "--select",
        type=str,
        default=None,
        help="Select a character to use.",
    )

    sub_parsers = parser.add_subparsers(
        metavar='command',
        dest='cmd',
    )

    sub_parsers.required = False

    configure_parser_create(sub_parsers)
    configure_parser_list(sub_parsers)

    args = parser.parse_args()
    if args.select:
        select_character(args)
    if  hasattr(args, "func"):
        args.func(args)
    return


if __name__ == "__main__":
    main()
