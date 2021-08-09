import datetime

from MonsterLab.monster_data import Random


class Monster:

    def __init__(self, name=None, monster_type=None, level=None, rarity=None):
        self.type = monster_type or Random.random_type()
        self.name = name or Random.random_name(self.type)
        self.level = level or Random.random_level()
        self.rarity = rarity or Random.random_rank()
        self.damage = f"{self.level}d{Random.dice[self.rarity]}{Random.bonus()}"
        self.time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.health = Random.resource(self.level, self.rarity)
        self.energy = Random.resource(self.level, self.rarity)
        self.sanity = Random.resource(self.level, self.rarity)

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
