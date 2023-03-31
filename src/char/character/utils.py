import os
import logging
from pathlib import Path

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
        LOGGER.warning("Failed to create directory {} for 5e CLI", CHAR_SAVE_PATH)
        raise e
