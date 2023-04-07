from unittest.mock import patch

from char.character.character import CharacterFactory

@patch('char.character.character.Character.save')
def test_characterfactory(*args):

    char_name = "name"

    char = CharacterFactory.create_char(char_name, "Human", "Barbarian")

    assert str(char) == char_name



