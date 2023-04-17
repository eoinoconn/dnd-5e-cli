from unittest import TestCase
from unittest.mock import patch, mock_open
import tempfile
import json
import os

from char.character.character import CharacterFactory
from char.character.utils import CHAR_SAVE_PATH

# Test character representation
TEST_CHAR_JSON = {
    "name": "Gandalf",
    "race": "Human",
    "cls": "Barbarian",
    "level": 1,
    "experience_points": 0,
    "strength": 15,
    "dexterity": 14,
    "constitution": 13,
    "intelligence": 12,
    "wisdom": 10,
    "charisma": 8,
    "hit_points": 0,
    "hit_dice": [],
    "speed": 0,
    "initiative": 0,
    "proficiencies": [],
    "languages": [],
    "equipment": [],
    "features": [],
    "spells": [],
}

class TestCharacterFactory(TestCase):

    def test_create_char(self):

        with tempfile.TemporaryDirectory() as temp_dir:
            with patch('char.character.character.CHAR_SAVE_PATH', temp_dir):
                char = CharacterFactory.create_char(
                    TEST_CHAR_JSON['name'], 
                    TEST_CHAR_JSON['race'], 
                    TEST_CHAR_JSON['cls']
                    )

                self.assertTrue(os.path.exists(os.path.join(temp_dir, TEST_CHAR_JSON['name'] + ".json")))

        self.assertEqual(str(char), TEST_CHAR_JSON["name"])
        self.assertEqual(char.race, TEST_CHAR_JSON['race'])
        self.assertEqual(char.cls, TEST_CHAR_JSON['cls'])

    @patch('builtins.open', new_callable=mock_open)
    def test_invalid_name_invalid_character(self, *args):
        """
        Test that an invalid name raises a ValueError.
        """
        args = [
            "Gand@lf the Grey",
            TEST_CHAR_JSON['race'], 
            TEST_CHAR_JSON['cls']]

        self.assertRaises(ValueError, CharacterFactory.create_char, *args)

    @patch('builtins.open', new_callable=mock_open)
    def test_invalid_name_length(self, *args):
        """
        Test that an invalid name raises a ValueError.
        """
        args = [
            "Gandalf the Grey also known as the white wizard",
            TEST_CHAR_JSON['race'], 
            TEST_CHAR_JSON['cls']]

        self.assertRaises(ValueError, CharacterFactory.create_char, *args)

    @patch('builtins.open', new_callable=mock_open)
    def test_invalid_name_empty(self, *args):
        """
        Test that an invalid name raises a ValueError.
        """
        args = [
            "",
            TEST_CHAR_JSON['race'], 
            TEST_CHAR_JSON['cls']]

        self.assertRaises(ValueError, CharacterFactory.create_char, *args)

    def test_char_already_exists(self, *args):
        args = [
            TEST_CHAR_JSON['name'],
            TEST_CHAR_JSON['race'], 
            TEST_CHAR_JSON['cls']]

        with tempfile.TemporaryDirectory() as temp_dir:
            with patch('char.character.character.CHAR_SAVE_PATH', temp_dir):
                char = CharacterFactory.create_char(*args)

                self.assertRaises(ValueError, CharacterFactory.create_char, *args)


