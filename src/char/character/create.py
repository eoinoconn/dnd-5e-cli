"""
Module for creating a character.
"""
import logging

from PyInquirer import prompt

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

    @staticmethod
    def create_from_cli():
        """
        Create a character from the command line.
        """
        print("Creating a new character...")
        questions = [
            {
                'type': 'input',
                'name': 'name',
                'message': "what\'s your name?"
            },
            {
                'type': 'list',
                'name': 'race',
                'message': 'What\'s your race?',
                'choices': fifth_edition.races_list
            },
            {
                'type': 'list',
                'name': 'class',
                'message': 'What\'s your class?',
                'choices': fifth_edition.classes_list
            }
        ]
        answers = prompt(questions)
        LOGGER.info(answers)

        char = CharacterFactory.create_char(
            answers["name"],
            answers["race"],
            answers["class"]
        )
        print(f"Created a new character: {char}")


def execute(*args):
    """
    Creates character from command line.
    """
    CharacterCreator.create_from_cli()
