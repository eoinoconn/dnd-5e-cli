import logging
import os
import shutil
import setuptools

from src.char.config import get_app_config
cfg = get_app_config()

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

def create_dir_structure(config):
    """
    Creates fodler necessary for cli character saving.
    """
    try:
        if not os.path.isdir(config.CHAR_SAVE_PATH):
            os.makedirs(config.CHAR_SAVE_PATH)
    except (FileExistsError, FileNotFoundError) as e:
        LOGGER.warning(
            "Failed to create directory %s for 5e CLI", str(config.CHAR_SAVE_PATH))
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

# establish data directory.
create_dir_structure(cfg)

# create config file.
create_config_file(cfg.SAVE_PATH, "config/default_config.yaml")

setuptools.setup(
    name="dnd-5e-cli",
    version="0.0.1",
    author="Eoin OConnell",
    author_email="eoinoconn@gmail.com",
    description="A simple DnD CLI tool.",
    url="https://github.com/eoinoconn/dnd-5e-cli",
    project_urls={
        "Bug Tracker": "https://github.com/eoinoconn/dnd-5e-cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="./src"),
    python_requires=">=3.6",
)