from unittest.mock import patch

from char.character import character
from char.character.create import CharacterCreator
from char import fifth_edition

user_entrys = [
    {'name': 'eoin'},
    {'race': fifth_edition.races_list[0]},
    {'class': fifth_edition.classes_list[0]}
]

@patch('char.character.create.prompt', side_effect=user_entrys)
@patch('char.character.character.Character.save')
def test_character_creator(save_patch, promt_patch):
    """
    Test simple character creation.
    """
    CharacterCreator.create_from_cli()