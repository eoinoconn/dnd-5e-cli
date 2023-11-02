import os
from pathlib import Path


class AppConfig:
    SAVE_PATH = os.path.join(str(Path.home()), ".5e_cli")
    CHAR_SAVE_PATH = os.path.join(SAVE_PATH, "chars")