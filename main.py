from time import sleep

from MonsterLab import Monster


def print_mobs():
    for rarity in [f"Rank {r}" for r in range(1, 6)]:
        for level in range(1, 11):
            sleep(1)
            print(Monster(level=level, rarity=rarity))


if __name__ == '__main__':
    print_mobs()
