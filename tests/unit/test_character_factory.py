from char.character.character import CharacterFactory


def test_characterfactory():

    char_name = "name"

    char = CharacterFactory.create_char(char_name, "race", "cls")

    assert str(char) == char_name



