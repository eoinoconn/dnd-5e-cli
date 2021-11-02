from logging import getLogger

from PyInquirer import prompt

from char import fifth_edition

LOGGER = getLogger(__name__)

class CharacterCreator:

    @staticmethod
    def create_from_cli():
        """
        """
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
                'choices': fifth_edition.races
            },
            {
                'type': 'list',
                'name': 'class',
                'message': 'What\'s your class?',
                'choices': fifth_edition.classes
            }
        ]
        answers = prompt(questions)
        print(answers) 
        

def execute(*args):
    CharacterCreator.create_from_cli()


