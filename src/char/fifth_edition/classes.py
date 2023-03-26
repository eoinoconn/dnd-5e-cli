"""
Character classes.
"""
from abc import ABC, abstractmethod

classes_list = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]


def get_class(class_str):
    """
    Get a class by name.

    :param class_str: The name of the class.

    :return: The class.

    :raises: ValueError if the class is not found.
    """
    if class_str == "Barbarian":
        return Barbarian()
    else:
        raise ValueError("Class not implemented")


class Class(ABC):
    """
    Class parent class.
    """

    @abstractmethod
    def update_character(self, char):
        pass

    @abstractmethod
    def update_ability_scores():
        pass

    @abstractmethod
    def update_skills():
        pass

    @abstractmethod
    def update_spells():
        pass

class Barbarian(Class):
    """
    Barbarian class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the barbarian class.
        
        :param char: The character to update.
        """
        char.cls = "Barbarian"

        self.update_ability_scores()
        self.update_skills()
        self.update_spells()

    @staticmethod
    def update_ability_scores():
        pass

    @staticmethod
    def update_skills():
        pass

    @staticmethod
    def update_spells():
        pass

classes = {
    "Barbarian": Barbarian,
}