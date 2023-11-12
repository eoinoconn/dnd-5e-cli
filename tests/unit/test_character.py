import os
import tempfile
import unittest
from char.character.character import CharacterFactory
from char.config import get_app_config

cfg = get_app_config()

class TestWriteCharacterFactory(unittest.TestCase):
    def setUp(self):
        # create temporary directory for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.save_dir = self.temp_dir.name
        cfg.CHAR_SAVE_PATH = self.save_dir

        # create a temporary YAML file for testing
        self.config_file = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml")
        self.config_path = self.config_file.name

        # copy the contents of the example file to the temporary file
        with open("config/default_config.yaml", "r") as example_file:
            with open(self.config_path, "w") as temp_file:
                temp_file.write(example_file.read())

    def test_characterfactory(self):

        char_name = "name"
        char_race = "Human"
        char_class = "Barbarian"

        char = CharacterFactory.create_char(char_name, char_race, char_class)

        assert str(char) == char_name
        assert char.race == char_race
        assert char.cls == char_class

    def tearDown(self):
        # delete the temporary directory
        self.temp_dir.cleanup()

        # delete the temporary file
        os.remove(self.config_path)
