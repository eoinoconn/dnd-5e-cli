from unittest.mock import patch

from char.character.create import CharacterCreator
from char import fifth_edition

user_entrys = [
    {'name': 'eoin'},
    {'race': fifth_edition.races_list[0]},
    {'class': fifth_edition.classes_list[0]}
]

@patch('char.character.create.prompt', side_effect=user_entrys)
def test_character_creator(input):
    """
    Test simple character creation.
    """
    CharacterCreator.create_from_cli()