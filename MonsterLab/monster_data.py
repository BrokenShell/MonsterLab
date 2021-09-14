from collections import deque
from math import sqrt
from random import shuffle, triangular, choice, random, randrange, randint
from typing import Iterable, Any


class TruffleShuffle:
    """ Truffle Shuffle
    Please refer to https://pypi.org/project/Fortuna/ for full documentation.
    """
    __slots__ = ("flat", "data", "rotate_size", "size")

    def __init__(self, collection: Iterable[Any]):
        tmp_data = list(collection)
        shuffle(tmp_data)
        self.data = deque(tmp_data)
        self.size = len(self.data)
        self.rotate_size = int(sqrt(self.size))

    def __call__(self) -> Any:
        self.data.rotate(int(triangular(1, self.rotate_size, self.size)))
        selection = self.data[-1]
        if callable(selection):
            return selection()
        else:
            return selection


def plus_or_minus(num: int) -> int:
    return randrange(-num, num+1)


def percent_true(num: int = 50) -> bool:
    return randint(1, 100) <= num


class Random:
    dragon_type = TruffleShuffle([
        "Platinum",
        "Gold",
        "Silver",
        "Bronze",
        "Brass",
        "Copper",
        "Black",
        "Blue",
        "Green",
        "Red",
        "White",
        "Onyx",
        "Sapphire",
        "Emerald",
        "Ruby",
        "Diamond",
        "Prismatic",
    ])

    element = TruffleShuffle([
        "Lightning",
        "Flame",
        "Spore",
        "Ice",
        "Steam",
        "Mud",
        "Dust",
        "Smoke",
        "Magma",
        "Shadow",
    ])

    character_type = TruffleShuffle([
        "Mage",
        "Guard",
        "Villager",
        "Archer",
        "Knight",
    ])

    archfey_type = TruffleShuffle((
        lambda: Random.dragon_type(),
        lambda: Random.element(),
    ))

    monsters_by_type = {
        "Fey": (
            lambda: f"{Random.dragon_type()} Faerie",
            lambda: f"{Random.element()} Spirit",
            lambda: f"{Random.archfey_type()} Archfey",
        ),
        "Demonic": (
            "Imp",
            "Quasit",
            lambda: f"{Random.dragon_type()} Demon",
            "Hell Hound",
            "Night Hag",
            "Nightmare",
            "Hook Horror",
            "Pit Fiend",
            "Balor",
        ),
        "Devilkin": (
            lambda: f"Goblin {Random.character_type()}",
            lambda: f"Kobold {Random.character_type()}",
            lambda: f"{Random.element()} Devil",
            lambda: f"{'Succubus' if percent_true(75) else 'Incubus'}",
            "Pit Lord",
            "Prince of Fear",
        ),
        "Dragon": (
            lambda: f"{Random.dragon_type()} Wyrmling",
            lambda: f"{Random.dragon_type()} Drake",
            lambda: f"{Random.dragon_type()} Dragon",
            "Faerie Dragon",
            "Pseudodragon",
            "Wyvern",
        ),
        "Elemental": (
            lambda: f"{Random.element()} Mephit",
            lambda: f"{Random.element()} Elemental",
            "Djinni",
            "Efreeti",
        ),
        "Undead": (
            lambda: f"Zombie {Random.character_type()}",
            lambda: f"Skeletal {Random.character_type()}",
            lambda: f"Ghostly {Random.character_type()}",
            "Ghoul",
            "Banshee",
            "Wraith",
            "Ghast",
            "Wight",
            "Revenant",
            "Mummy",
            "Vampire",
            "Lich",
            "Dracolich",
            "Poltergeist",
            "Death Knight",
            "Mummy Lord",
            "Demilich",
            "Lich King",
        ),
    }
    rank_options = [
        "Rank 0",
        "Rank 1",
        "Rank 2",
        "Rank 3",
        "Rank 4",
        "Rank 5",
    ]
    dice_options = [2, 4, 6, 8, 10, 12]
    dice = dict(zip(rank_options, dice_options))
    var_options = range(len(rank_options))
    variance = dict(zip(rank_options, var_options))
    random_type = TruffleShuffle(monsters_by_type.keys())

    @staticmethod
    def bonus():
        roll = int(triangular(0, 6, 0))
        return f"{f'+{roll}' if roll > 0 else f''}"

    @staticmethod
    def resource(level, rank):
        return round(sum((
            random() if percent_true(50) else -random(),
            plus_or_minus(Random.variance[rank]),
            level * Random.dice[rank],
        )), 2)

    @staticmethod
    def random_level():
        return int(triangular(1, 21, 3))

    def random_rank(self):
        group = list(self.dice.keys())
        return group[int(triangular(0, len(group), 0))]

    def random_name(self, monster_type=None):
        if monster_type:
            monster = choice(self.monsters_by_type[monster_type])
        else:
            monster = choice(self.monsters_by_type[self.random_type()])
        if callable(monster):
            return monster()
        else:
            return monster
