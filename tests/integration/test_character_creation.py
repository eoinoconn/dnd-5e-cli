from unittest.mock import patch

from char.character.create import CharacterCreator
from char import fifth_edition

user_entrys = [
    {'name': 'eoin'},
    {'race': list(fifth_edition.races.keys())[0]},
    {'class': list(fifth_edition.classes.keys())[0]}
]

@patch('char.character.create.prompt', side_effect=user_entrys)
def test_character_creator(input):
    """
    Test simple character creation.
    """
    CharacterCreator.create_from_cli()