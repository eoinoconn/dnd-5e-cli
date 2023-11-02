import os
import logging
import re
import json

from char.config import AppConfig as cfg

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S%p')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

def get_config_path(config) -> str:
    """
    Returns the path to the config file.
    """
    return os.path.join(config.SAVE_PATH, "default_config.yaml")

def check_if_char_exists(char_save_file):
    """
    Checks if a character with the given name already exists.
    """
    if os.path.isfile(char_save_file):
        raise ValueError("Character already exists.")


def check_char_name(char_name):
    """
    Checks if the character name is valid.

    Character name must be:
        - a string and not empty.
        - not contain any special characters.
        - not be longer than 30 characters.

    Check is performed using Regex.

    Args:
        char_name (str): Character name.

    Returns:
        bool: True if character name is valid, False otherwise.
    """
    if not isinstance(char_name, str):
        return False
    if not char_name:
        return False
    if len(char_name) > 30:
        return False
    if re.search(r"[^a-zA-Z0-9_]", char_name):
        return False
    return True


def get_char_save_file_name(save_dir, char_name):
    """
    Returns file name friendly version of the character 
    name. Replaces whitespace with underscore and
    converts to lowercase.

    Args:
        char_name (str): Character name.

    Returns:
        str: File name friendly version of the character name.
    """
    return os.path.join(save_dir, char_name.replace(" ", "_")) + ".json"


def get_char_save_files(save_dir: str = cfg.CHAR_SAVE_PATH):
    """
    Returns a list of all character save files in the given directory.

    Args:
        save_dir (str): Directory to search for character save files.

    Returns:
        list: List of character save files.
    """
    return [os.path.join(save_dir, f) for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))]

def list_char_names(save_dir: str = cfg.CHAR_SAVE_PATH):
    """
    Returns a list of all character names in the given directory.

    Args:
        save_dir (str): Directory to search for character save files.

    Returns:
        list: List of character names.
    """
    char_names = []
    for f in get_char_save_files(save_dir):
        with open(f, "r") as char_file:
            char =json.load(char_file)
            char_names.append(char["name"])

    return char_names
