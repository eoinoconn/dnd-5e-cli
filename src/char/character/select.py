# Module for chacter slection.
import argparse

from char.config import get_app_config

from .utils import list_char_names

cfg = get_app_config()

def select_character(args: argparse.Namespace, char_save_path=cfg.CHAR_SAVE_PATH) -> None:
    """Select a character to use."""

    char_names = [name.lower() for name in list_char_names(save_dir=char_save_path)]

    if args.select.lower() in char_names:
        print(f"Selecting character: {args.select}")
        cfg.selected_character = args.select.lower()

    else:
        print(f"Character: {args.select} does not exist.")
        print(f"Create it using 'char create {args.select}'")
    
