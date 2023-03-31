"""
Module for creating a character.
"""
import logging

from PyInquirer import prompt
from textwrap import dedent

from char import fifth_edition

from .character import CharacterFactory

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class CharacterCreator:
    """
    Character creator class.
    """

    def create():
        pass

    @classmethod
    def create_from_cli(self):
        """
        Create a character from the command line.
        """
        print("Creating a new character...")

        character_rep = {}

        character_rep.update(self.ask_for_char_name())
        # TODO: Check if name exists
        character_rep.update(self.ask_for_char_race())
        character_rep.update(self.ask_for_char_class())

        LOGGER.debug(character_rep)

        char = CharacterFactory.create_char(
            character_rep["name"],
            character_rep["race"],
            character_rep["class"]
        )

        # TODO: save character to disk.

        print(f"Welcome {char.name}")

        return char

    @staticmethod
    def ask_for_char_name():
        """
        Ask user for character name.
        """
        return prompt({
            'type': 'input',
            'name': 'name',
            'message': "what\'s your name?"
            })

    @staticmethod
    def ask_for_char_race():
        """
        Ask for char race.
        """
        return prompt({
            'type': 'list',
            'name': 'race',
            'message': 'What\'s your race?',
            'choices': fifth_edition.races_list
            })

    @staticmethod
    def ask_for_char_class():
        """
        Ask for char class
        """
        return prompt({
            'type': 'list',
            'name': 'class',
            'message': 'What\'s your class?',
            'choices': fifth_edition.classes_list
            })


def execute(*args):
    """
    Creates character from command line.
    """
    CharacterCreator.create_from_cli()


def configure_parser_create(sub_parser) -> None:
    help = ""
    descr = (help + "") #TODO: Fill this in

    example = dedent("""
    Examples:
        char create
    """)
    parser = sub_parser.add_parser(
        'create',
        description=descr,
        help=help,
        epilog=example,
    )

    parser.set_defaults(func=execute)
