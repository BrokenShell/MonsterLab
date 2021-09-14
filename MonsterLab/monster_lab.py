from datetime import datetime

import pytz

from MonsterLab.monster_data import Random


class Monster:

    def __init__(self, name=None, monster_type=None, level=None, rarity=None):
        rand = Random()
        self.type = monster_type or rand.random_type()
        self.name = name or rand.random_name(self.type)
        self.level = level or rand.random_level()
        self.rarity = rarity or rand.random_rank()
        self.damage = f"{self.level}d{rand.dice[self.rarity]}{rand.bonus()}"
        lambda_time = pytz.timezone('US/Pacific')
        self.time_stamp = datetime.now(lambda_time).strftime("%Y-%m-%d %H:%M:%S")
        self.health = rand.resource(self.level, self.rarity)
        self.energy = rand.resource(self.level, self.rarity)
        self.sanity = rand.resource(self.level, self.rarity)

    def to_dict(self):
        return {
            "Name": self.name,
            "Type": self.type,
            "Level": self.level,
            "Rarity": self.rarity,
            "Damage": self.damage,
            "Health": self.health,
            "Energy": self.energy,
            "Sanity": self.sanity,
            "Time Stamp": self.time_stamp,
        }

    def __repr__(self):
        output = (f"{key}: {val}" for key, val in self.to_dict().items())
        return "\n".join(output)

    def __str__(self):
        return self.__repr__() + "\n"
