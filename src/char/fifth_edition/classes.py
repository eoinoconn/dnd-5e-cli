"""
Character classes.
"""
from abc import ABC, abstractmethod


#TODO: is this needed?
def get_class(class_str):
    """
    Get a class by name.

    :param class_str: The name of the class.

    :return: The class.

    :raises: ValueError if the class is not found.
    """
    if class_str == "Barbarian":
        return Barbarian()
    elif class_str == "Bard":
        return Bard()
    elif class_str == "Cleric":
        return Cleric()
    elif class_str == "Druid":
        return Druid()
    elif class_str == "Fighter":
        return Fighter()
    elif class_str == "Monk":
        return Monk()
    elif class_str == "Paladin":
        return Paladin()
    elif class_str == "Ranger":
        return Ranger()
    elif class_str == "Rogue":
        return Rogue()
    elif class_str == "Sorcerer":
        return Sorcerer()
    elif class_str == "Warlock":
        return Warlock()
    elif class_str == "Wizard":
        return Wizard()
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

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Bard(Class):
    """
    Bard class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the bard class.
        
        :param char: The character to update.
        """
        char.cls = "Bard"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Cleric(Class):
    """
    Cleric class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the cleric class.
        
        :param char: The character to update.
        """
        char.cls = "Cleric"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Druid(Class):
    """
    Druid class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the druid class.
        
        :param char: The character to update.
        """
        char.cls = "Druid"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Fighter(Class):
    """
    Fighter class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the fighter class.
        
        :param char: The character to update.
        """
        char.cls = "Fighter"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Monk(Class):
    """
    Monk class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the monk class.
        
        :param char: The character to update.
        """
        char.cls = "Monk"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Paladin(Class):
    """
    Paladin class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the paladin class.
        
        :param char: The character to update.
        """
        char.cls = "Paladin"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Ranger(Class):
    """
    Ranger class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the ranger class.
        
        :param char: The character to update.
        """
        char.cls = "Ranger"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Rogue(Class):
    """
    Rogue class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the rogue class.
        
        :param char: The character to update.
        """
        char.cls = "Rogue"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Sorcerer(Class):
    """
    Sorcerer class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the sorcerer class.
        
        :param char: The character to update.
        """
        char.cls = "Sorcerer"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Warlock(Class):
    """
    Warlock class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the warlock class.
        
        :param char: The character to update.
        """
        char.cls = "Warlock"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

class Wizard(Class):
    """
    Wizard class.
    """
    @classmethod
    def update_character(self, char):
        """
        Update the character with the wizard class.
        
        :param char: The character to update.
        """
        char.cls = "Wizard"

        self.update_ability_scores(char)
        self.update_skills(char)
        self.update_spells(char)

    def update_ability_scores(char):
        pass

    def update_skills(char):
        pass

    def update_spells(char):
        pass

classes = {
    "Barbarian": Barbarian,
    "Bard": Bard,
    "Cleric": Cleric,
    "Druid": Druid,
    "Fighter": Fighter,
    "Monk": Monk,
    "Paladin": Paladin,
    "Ranger": Ranger,
    "Rogue": Rogue,
    "Sorcerer": Sorcerer,
    "Warlock": Warlock,
    "Wizard": Wizard
}