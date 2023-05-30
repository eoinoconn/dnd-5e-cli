# Module for chacter slection.
import argparse
import yaml
from textwrap import dedent

from .utils import list_char_names, get_config_path, CHAR_SAVE_PATH

def write_character_selection(name: str, config_path: str) -> None:
    """
    Write the selected character to the config file.
    """
    # open config file.
    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    # write character name to config file.
    config["selected_character"] = name

    # write config file.
    with open(config_path, "w") as config_file:
        yaml.safe_dump(config, config_file)

def select_character(args: argparse.Namespace) -> None:
    """Select a character to use."""

    char_names = [name.lower() for name in list_char_names(save_dir=CHAR_SAVE_PATH)]

    if args.select.lower() in char_names:
        print(f"Selecting character: {args.select}")
        write_character_selection(args.select.lower(), get_config_path())

    else:
        print(f"Character: {args.select} does not exist.")
        print(f"Create it using 'char create {args.select}'")
    
def get_selected_character():
    """
    Returns the name of the currently selected character.
    """
    config_path = get_config_path()
    with open(config_path, "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        return config["selected_character"]
