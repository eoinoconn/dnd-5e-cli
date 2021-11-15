import argparse
from argparse import SUPPRESS
import logging

#from .. import __version__
from .character.utils import configure_parser_create

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def main():

    parser = argparse.ArgumentParser(
        allow_abbrev=False,
        description='List the content of a folder',
    )

    parser.add_argument(
        '-V', '--version',
        action='version',
        # version= f"5e {__version__}", #TODO: fill in
        help="Show the conda version number and exit."
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
    args.func(args)


if __name__ == "__main__":
    main()
