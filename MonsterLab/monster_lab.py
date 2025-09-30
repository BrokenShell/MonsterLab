from Fortuna import *


class MonsterLab:
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
        lambda: MonsterLab.dragon_type(),
        lambda: MonsterLab.element(),
    ))

    monsters_by_type = {
        "Fey": (
            lambda: f"{MonsterLab.dragon_type()} Faerie",
            lambda: f"{MonsterLab.element()} Spirit",
            lambda: f"{MonsterLab.archfey_type()} Archfey",
        ),
        "Demonic": (
            "Imp",
            "Quasit",
            lambda: f"{MonsterLab.dragon_type()} Demon",
            "Hell Hound",
            "Night Hag",
            "Nightmare",
            "Hook Horror",
            "Pit Fiend",
            "Balor",
        ),
        "Devilkin": (
            lambda: f"Goblin {MonsterLab.character_type()}",
            lambda: f"Kobold {MonsterLab.character_type()}",
            lambda: f"{MonsterLab.element()} Devil",
            lambda: f"{'Succubus' if percent_true(75) else 'Incubus'}",
            "Pit Lord",
            "Prince of Fear",
        ),
        "Dragon": (
            lambda: f"{MonsterLab.dragon_type()} Wyrmling",
            lambda: f"{MonsterLab.dragon_type()} Drake",
            lambda: f"{MonsterLab.dragon_type()} Dragon",
            "Faerie Dragon",
            "Pseudodragon",
            "Wyvern",
        ),
        "Elemental": (
            lambda: f"{MonsterLab.element()} Mephit",
            lambda: f"{MonsterLab.element()} Elemental",
            "Djinni",
            "Efreeti",
        ),
        "Undead": (
            lambda: f"Zombie {MonsterLab.character_type()}",
            lambda: f"Skeletal {MonsterLab.character_type()}",
            lambda: f"Ghostly {MonsterLab.character_type()}",
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
            canonical() if percent_true(50) else -canonical(),
            plus_or_minus(MonsterLab.variance[rank]),
            level * MonsterLab.dice[rank],
        )), 2)

    @staticmethod
    def random_level():
        return int(triangular(1, 21, 3))

    def random_rank(self):
        group = list(self.dice.keys())
        return group[int(triangular(0, len(group), 0))]

    def random_name(self, monster_type=None):
        if monster_type:
            monster = random_value(self.monsters_by_type[monster_type])
        else:
            monster = random_value(self.monsters_by_type[self.random_type()])
        if callable(monster):
            return monster()
        else:
            return monster
