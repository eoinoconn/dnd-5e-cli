import os
import json

def setup_char_json(save_loc, char_json):
    """
    Save a character json file for testing.
    """
    char_path = os.path.join(save_loc, char_json["name"] + ".json")
    with open(char_path, "w") as f:
        json.dump(char_json, f)

def teardown_char_json(save_loc, char_json):
    """
    Delete character json file
    """
    char_path = os.path.join(save_loc, char_json["name"] + ".json")
    os.remove(char_path)