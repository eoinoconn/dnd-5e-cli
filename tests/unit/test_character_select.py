import json
import os
import yaml
import tempfile
import unittest
import argparse

from unittest.mock import patch
from char.character.select import select_character


class TestSelectCharacter(unittest.TestCase):
    def setUp(self):
        # create a temporary directory for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = self.temp_dir.name

        # create a temporary YAML file in the temporary directory for testing
        self.config_path = os.path.join(self.temp_path, "default_config.yaml")

        # create a subdirectory for character files
        os.mkdir(os.path.join(self.temp_path, "chars"))

        # copy the contents of the example file to the temporary file
        with open("config/default_config.yaml", "r") as example_file:
            with open(self.config_path, "w") as temp_file:
                temp_file.write(example_file.read())

    def tearDown(self):
        # delete the temporary file after testing
        os.remove(self.config_path)

    # patch the config path to point to the temporary file
    @patch("char.character.select.cfg.get_config_path")
    def test_selects_existing_character(self, mock_config_path):
        # arrange
        args = argparse.Namespace(select="mario")
        # create character json
        char_path = os.path.join(self.temp_path, "chars", "mario.json")
        with open(char_path, "w") as char_file:
            json.dump( {"name": "mario"}, char_file)

        # set the config path to the temporary file
        mock_config_path.return_value = self.config_path

        # act
        select_character(args, os.path.join(self.temp_path, "chars"))

        # assert
        with open(self.config_path, "r") as config_file:
            config = yaml.safe_load(config_file)
            self.assertEqual(config["selected_character"], "mario")

    def test_does_not_select_nonexistent_character(self):
        # arrange
        args = argparse.Namespace(select="nonexistent")

        # act
        select_character(args)

        # assert
        with open(self.config_path, "r") as config_file:
            config = yaml.safe_load(config_file)
            self.assertNotEqual(config["selected_character"], "nonexistent")

    @patch("char.character.select.cfg.get_config_path")
    def test_select_character_with_different_case(self, mock_config_path):
        # arrange
        args = argparse.Namespace(select="Mario")
        # create character json
        char_path = os.path.join(self.temp_path, "chars", "mario.json")
        with open(char_path, "w") as char_file:
            json.dump( {"name": "mario"}, char_file)

        # set the config path to the temporary file
        mock_config_path.return_value = self.config_path

        # act
        select_character(args, os.path.join(self.temp_path, "chars"))

        # assert
        with open(self.config_path, "r") as config_file:
            config = yaml.safe_load(config_file)
            self.assertEqual(config["selected_character"], "mario")

    def test_prints_error_message_for_nonexistent_character(self):
        # arrange
        args = argparse.Namespace(select="nonexistent")

        # act
        with patch("builtins.print") as mock_print:
            select_character(args)

        # assert
        mock_print.assert_called_with("Create it using 'char create nonexistent'")

if __name__ == '__main__':
    unittest.main()