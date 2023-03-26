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
    "Halfling",
    "Half-Orc",
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


class Human(Race):

    @classmethod
    def update_character(char):
        char.race = "Human"

    @abstractmethod
    def update_ability_scores():
        pass

    @abstractmethod
    def update_skills():
        pass

    @abstractmethod
    def update_spells():
        pass


class Dragonborn(Race):

    @staticmethod
    def update_character(char):
        char.race = "Dragonborn"

    def update_ability_scores(self, char):
        char.ability_scores["Strength"] += 2
        char.ability_scores["Charisma"] += 1

    def update_skills(self, char):
        pass

    def update_spells(self, char):
        pass


races = {
    "Human": Human,
    "Dragonborn": Dragonborn,
}
