"""
Character class.
"""


class Character:

    def __init__(self, name):
        """
        Character class.

        :param name: The name of the character.
        """
        self.name = name
        self.race = None
        self.cls = None

        self.level = 1
        self.experience_points = 0

        self.strength = 15
        self.dexterity = 14
        self.constitution = 13
        self.intelligence = 12
        self.wisdom = 10
        self.charisma = 8

        self.hit_points = 0
        self.hit_dice = []
        self.speed = 0
        self.initiative = 0

        self.proficiencies = []
        self.languages = []
        self.equipment = []
        self.features = []
        self.spells = []

    @property
    def acrobatics(self):
        """
        Return the acrobatics modifier.
        """
        if "acrobatics" in self.proficiencies:
            return self.dexterity + self.proficiency_bonus
        return self.dexterity

    @property
    def animal_handling(self):
        """
        Return the animal handling modifier.
        """
        if "animal_handling" in self.proficiencies:
            return self.wisdom + self.proficiency_bonus
        return self.wisdom

    @property
    def arcana(self):
        """
        Return the arcana modifier.
        """
        if "arcana" in self.proficiencies:
            return self.intelligence + self.proficiency_bonus
        return self.intelligence

    @property
    def athletics(self):
        if "athletics" in self.proficiencies:
            return self.strength + self.proficiency_bonus
        return self.strength

    @property
    def deception(self):
        if "deception" in self.proficiencies:
            return self.charisma + self.proficiency_bonus
        return self.charisma

    @property
    def history(self):
        if "history" in self.proficiencies:
            return self.intelligence + self.proficiency_bonus
        return self.intelligence

    @property
    def insight(self):
        if "insight" in self.proficiencies:
            return self.wisdom + self.proficiency_bonus
        return self.wisdom

    @property
    def intimidation(self):
        if "intimidation" in self.proficiencies:
            return self.charisma + self.proficiency_bonus
        return self.charisma

    @property
    def investigation(self):
        if "investigation" in self.proficiencies:
            return self.intelligence + self.proficiency_bonus
        return self.intelligence

    @property
    def medicine(self):
        if "medicine" in self.proficiencies:
            return self.wisdom + self.proficiency_bonus
        return self.wisdom

    @property
    def nature(self):
        if "nature" in self.proficiencies:
            return self.intelligence + self.proficiency_bonus
        return self.intelligence

    @property
    def perception(self):
        if "perception" in self.proficiencies:
            return self.wisdom + self.proficiency_bonus
        return self.wisdom

    @property
    def persuasion(self):
        if "persuasion" in self.proficiencies:
            return self.charisma + self.proficiency_bonus
        return self.charisma

    @property
    def religion(self):
        if "religion" in self.proficiencies:
            return self.intelligence + self.proficiency_bonus
        return self.intelligence

    @property
    def sleight_of_hand(self):
        if "sleight_of_hand" in self.proficiencies:
            return self.dexterity + self.proficiency_bonus
        return self.dexterity

    @property
    def stealth(self):
        if "stealth" in self.proficiencies:
            return self.dexterity + self.proficiency_bonus
        return self.dexterity

    @property
    def survival(self):
        if "survival" in self.proficiencies:
            return self.wisdom + self.proficiency_bonus
        return self.wisdom

    @property
    def armour_class(self):
        return 10 + self.dexterity_modifier

    @property
    def strength_modifier(self):
        return self.strength // 2 - 5

    @property
    def dexterity_modifier(self):
        return self.dexterity // 2 - 5

    @property
    def constitution_modifier(self):
        return self.constitution // 2 - 5

    @property
    def inteligence_modifier(self):
        return self.intelligence // 2 - 5

    @property
    def wisdom_modifier(self):
        return self.wisdom // 2 - 5

    @property
    def charrima_modifier(self):
        return self.charisma // 2 - 5

    @property
    def proficiency_bonus(self):
        return self.level // 4 + 2

    @property
    def passive_perception(self):
        return 10 + self.perception

    @property
    def passive_investigation(self):
        return 10 + self.investigation

    @property
    def passive_insight(self):
        return 10 + self.insight

    @property
    def hit_points_max(self):
        hit_points_max = 0
        for dice in self.hit_dice:
            hit_points_max = max(dice, hit_points_max)

        return hit_points_max

    def __str__(self):
        return self.name


class CharacterFactory:

    @staticmethod
    def create_char(name, race, cls):

        char = Character(name)

        # TODO: add race
        # fifth_edition.get_race[race].add_specifics(char)

        # TODO: Add class specifics
        # fifth_edition.get_class[cls].add_specifics(char)

        # TODO: Choose proficiences

        return char
