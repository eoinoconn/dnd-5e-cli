import os
import logging
from pathlib import Path
import re
import shutil
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

def create_dir_structure(config):
    """
    Creates fodler necessary for cli character saving.
    """
    try:
        if not os.path.isdir(config.CHAR_SAVE_PATH):
            os.makedirs(config.CHAR_SAVE_PATH)
    except (FileExistsError, FileNotFoundError) as e:
        LOGGER.warning(
            f"Failed to create directory {str(config.CHAR_SAVE_PATH)} for 5e CLI")
        raise e

def create_config_file(
        config_dir: str = cfg.SAVE_PATH, 
        config_file: str = "default_config.yaml"
        ):
    """
    Copies the file config_file to the user's data directory.
    """
    # check if config_dir exists else raise error.
    if not os.path.isdir(config_dir):
        raise FileNotFoundError(
            "Config directory {config_dir} does not exist.")

    try:
        shutil.copy2(config_file, config_dir)
    except (FileExistsError, FileNotFoundError) as e:
        LOGGER.warning(
            "Failed to create config file %s for 5e CLI", config_file)
        raise e

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
