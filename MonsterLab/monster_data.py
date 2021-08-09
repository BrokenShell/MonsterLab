from Fortuna import QuantumMonty, FlexCat, front_linear
from Fortuna import canonical, percent_true, plus_or_minus


class Random:
    dragon_type = QuantumMonty([
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
    ]).middle_gauss

    element = QuantumMonty([
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
    ]).middle_gauss

    character = QuantumMonty([
        "Mage",
        "Guard",
        "Villager",
        "Archer",
        "Knight",
    ]).middle_gauss

    monsters_by_type = {
        "Fey": (
            lambda: f"{Random.dragon_type()} Faerie",
            lambda: f"{Random.element()} Spirit",
            lambda: f"{Random.dragon_type() if percent_true(50) else Random.element()} Archfey",
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
            lambda: f"Goblin {Random.character()}",
            lambda: f"Kobold {Random.character()}",
            lambda: f"{Random.element()} Devil",
            lambda: f"{'Succubus' if percent_true(75) else 'Incubus'}"
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
            lambda: f"Zombie {Random.character()}",
            lambda: f"Skeletal {Random.character()}",
            lambda: f"Ghostly {Random.character()}",
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
    random_level = QuantumMonty(range(1, 21)).front_poisson
    random_rank = QuantumMonty(dice.keys()).front_linear
    random_name = FlexCat(
        monsters_by_type,
        key_bias="truffle_shuffle",
        val_bias="front_linear",
    )
    random_type = random_name.random_cat

    @staticmethod
    def bonus():
        roll = front_linear(5)
        return f"{f'+{roll}' if roll > 0 else f''}"

    @staticmethod
    def resource(level, rank):
        return round(sum((
            canonical() if percent_true(50) else -canonical(),
            plus_or_minus(Random.variance[rank]),
            level * Random.dice[rank],
        )), 2)
