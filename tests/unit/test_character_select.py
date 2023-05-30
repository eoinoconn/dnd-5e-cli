import os
import yaml
import tempfile
import unittest
import argparse
import json
from unittest.mock import patch, mock_open
from char.character.select import select_character, write_character_selection, list_char_names, get_config_path


class TestWriteCharacterSelection(unittest.TestCase):
    def setUp(self):
        # create a temporary YAML file for testing
        self.config_file = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml")
        self.config_path = self.config_file.name

        # copy the contents of the example file to the temporary file
        with open("config/default_config.yaml", "r") as example_file:
            with open(self.config_path, "w") as temp_file:
                temp_file.write(example_file.read())

    def tearDown(self):
        # delete the temporary file after testing
        os.remove(self.config_path)

    def test_writes_selected_character_to_config_file(self):
        # arrange
        name = "Mario"

        # act
        write_character_selection(name, self.config_path)

        # assert
        with open(self.config_path, "r") as config_file:
            config = yaml.safe_load(config_file)
            self.assertEqual(config["selected_character"], name)

    def test_overwrites_existing_selected_character_in_config_file(self):
        # arrange
        name1 = "Mario"
        name2 = "Luigi"
        config = {"selected_character": name1}
        with open(self.config_path, "w") as config_file:
            yaml.safe_dump(config, config_file)

        # act
        write_character_selection(name2, self.config_path)

        # assert
        with open(self.config_path, "r") as config_file:
            config = yaml.safe_load(config_file)
            self.assertEqual(config["selected_character"], name2)

    def test_raises_exception_when_config_file_does_not_exist(self):
        # arrange
        name = "Mario"
        config_path = "nonexistent_file.yaml"

        # act/assert
        with self.assertRaises(FileNotFoundError):
            write_character_selection(name, config_path)

if __name__ == '__main__':
    unittest.main()