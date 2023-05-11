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
    def update_character(self, char):
        char.race = "Human"

        self.update_ability_scores()
        self.update_skills()
        self.update_spells()

    def update_ability_scores():
        pass

    def update_skills():
        pass

    def update_spells():
        pass


class Dragonborn(Race):

    @classmethod
    def update_character(self, char):
        char.race = "Dragonborn"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Dwarf(Race):

    @classmethod
    def update_character(self, char):
        char.race = "Dwarf"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Elf(Race):

    @classmethod
    def update_character(char):
        char.race = "Elf"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Gnome(Race):

    @classmethod
    def update_character(self, char):
        char.race = "Gnome"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class HalfElf(Race):

    @classmethod
    def update_character(self, char):
        char.race = "Half-Elf"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Halfling(Race):

    @classmethod
    def update_character(self, char):
        char.race = "Halfling"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class HalfOrc(Race):

    @classmethod
    def update_character(self, char):
        char.race = "Half-Orc"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Tiefling(Race):

    @classmethod
    def update_character(self, char):
        char.race = "Tiefling"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

races = {
    "Human": Human,
    "Dragonborn": Dragonborn,
    "Dwarf": Dwarf,
    "Elf": Elf,
    "Gnome": Gnome,
    "Half-Elf": HalfElf,
    "Halfling": Halfling,
    "Half-Orc": HalfOrc,
    "Tiefling": Tiefling
}
