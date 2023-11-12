import os
from pathlib import Path

import yaml

class SingletonClass:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

class AppConfig(SingletonClass):
    SAVE_PATH = os.path.join(str(Path.home()), ".5e_cli")
    CHAR_SAVE_PATH = os.path.join(SAVE_PATH, "chars")

    @property
    def selected_character(self):
        """
        Returns the name of the currently selected character.
        """
        config_path = self.get_config_path()
        with open(config_path, "r", encoding="utf-8") as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
            return config["selected_character"]


    @selected_character.setter
    def selected_character(self, char_name):
        """
        Sets the currently selected character.
        """
        config_path = self.get_config_path()
        # open config file.
        with open(config_path, "r",encoding="utf-8") as config_file:
            config = yaml.safe_load(config_file)

        # write character name to config file.
        config["selected_character"] = char_name

        # write config file.
        with open(config_path, "w",encoding="utf-8") as config_file:
            yaml.safe_dump(config, config_file)

    def get_config_path(self) -> str:
        """
        Returns the path to the config file.
        """
        return os.path.join(self.SAVE_PATH, "default_config.yaml")
    

def get_app_config():
    return AppConfig()