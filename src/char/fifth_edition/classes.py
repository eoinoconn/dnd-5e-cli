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
    if class_str == "Barbarian":
        return Barbarian()
    else:
        raise ValueError("Class not implemented")


class Class(ABC):

    def update_character(character):
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

    def update_ability_scores(self):
        pass

    def update_skills(self):
        pass

    def update_spells(self):
        pass
