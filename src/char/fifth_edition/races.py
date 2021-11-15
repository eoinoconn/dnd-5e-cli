"""
Character Races.
"""
from abc import ABC, abstractmethod

races_list = [
    "Dragonborn",
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling"
    "Half-Orc"
    "Human",
    "Tiefling"
]

class Race(ABC):

    @abstractmethod
    def update_character():
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


class Human:
    pass
