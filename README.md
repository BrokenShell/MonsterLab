# MonsterLab
by Robert Sharp

## Monster Class
### Optional Inputs
- Name
- Type
- Level
- Rarity

### Derived Fields
- Damage
- Health
- Energy
- Sanity
- Time Stamp

### Example Monster
- Name: Revenant
- Type: Undead
- Level: 3
- Rarity: Rank 0
- Damage: 3d2+1
- Health: 6.35
- Energy: 5.78
- Sanity: 6.0
- Time Stamp: 2021-08-09 14:23:23

### Code Example
```
$ pip install MonsterLab
$ python3
>>> from MonsterLab import Monster
>>> Monster()
Name: Imp
Type: Demonic
Level: 10
Rarity: Rank 0
Damage: 10d2+1
Health: 20.89
Energy: 20.55
Sanity: 20.79
Time Stamp: 2021-08-09 14:23:23
```
