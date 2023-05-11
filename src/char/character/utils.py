import os
import logging
from pathlib import Path
import regex as re

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S%p')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

SAVE_PATH = os.path.join(str(Path.home()), ".5e_cli")
CHAR_SAVE_PATH = os.path.join(SAVE_PATH, "chars")

def create_dir_structure():
    """
    Creates fodler necessary for cli character saving.
    """
    try:
        if not os.path.isdir(CHAR_SAVE_PATH):
            os.mkdir(CHAR_SAVE_PATH)
    except (FileExistsError, FileNotFoundError) as e:
        LOGGER.warning(
            "Failed to create directory {} for 5e CLI", CHAR_SAVE_PATH)
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


def get_char_save_files(save_dir: str = CHAR_SAVE_PATH):
    """
    Returns a list of all character save files in the given directory.

    Args:
        save_dir (str): Directory to search for character save files.

    Returns:
        list: List of character save files.
    """
    return [os.path.join(save_dir, f) for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))]
