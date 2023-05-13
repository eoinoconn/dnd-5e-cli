import unittest
import tempfile
import os

from char.character.utils import get_char_save_files, get_char_save_file_name, check_if_char_exists, create_config_file
from utils import setup_char_json


class TestCharacterUtils(unittest.TestCase):

    def test_get_char_save_files(self):
        # setup temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # setup character json
            setup_char_json(temp_dir, {"name": "test"})
            # test
            self.assertEqual(get_char_save_files(
                temp_dir), [temp_dir + "/test.json"])

    def test_get_char_save_file_name(self):
        self.assertEqual(get_char_save_file_name(
            "test", "test"), "test/test.json")

    def test_check_if_char_exists(self):
        # setup temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # setup character json
            setup_char_json(temp_dir, {"name": "test"})
            self.assertRaises(ValueError, check_if_char_exists,
                              temp_dir + "/test.json")

    def test_create_config_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            create_config_file(temp_dir, "config/default_config.yaml")
            self.assertTrue(os.path.isfile(temp_dir + "/default_config.yaml"))