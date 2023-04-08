import argparse
from argparse import SUPPRESS
import logging

#from .. import __version__
from .character.create import configure_parser_create
from .character.utils import create_dir_structure

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

    sub_parsers = parser.add_subparsers(
        metavar='command',
        dest='cmd',
    )

    sub_parsers.required = True

    configure_parser_create(sub_parsers)

    args = parser.parse_args()
    #args.func(args) TODO: fix this


if __name__ == "__main__":
    main()
