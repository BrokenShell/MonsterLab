# MonsterLab
by Robert Sharp

## Monster Class
### Optional Inputs
It is recommended to pass all the optional arguments or none of them. For example,
a custom type requires a custom name.
- Name: Compound Gaussian Distribution -> String
  - Derived from Type
  - Multidimensional distribution of types and subtypes
- Type: Wide Flat Distribution -> String
  - Demonic
  - Devilkin
  - Dragon
  - Undead
  - Elemental
  - Fey
  - Undead
- Level: Poisson Distribution -> Integer
  - Range: [1..20]
  - Most Common: [4..7] ~64%
  - Mean: 6.001
  - Median: 6
- Rarity: Linear Distribution [Rank 0..Rank 5] -> String
  - Rank 0: 30.5% Very Common
  - Rank 1: 25.0% Common
  - Rank 2: 19.4% Uncommon
  - Rank 3: 13.8% Rare
  - Rank 4: 8.3% Epic
  - Rank 5: 2.7% Legendary

### Derived Fields
- Damage: Compound Geometric Distribution with Linear Noise -> String
  - Derived from Level and Rarity
- Health: Geometric Distribution with Gaussian Noise -> Float
  - Derived from Level and Rarity
- Energy: Geometric Distribution with Gaussian Noise -> Float
  - Derived from Level and Rarity
- Sanity: Geometric Distribution with Gaussian Noise -> Float
  - Derived from Level and Rarity
- Time Stamp: The Monster's Birthday -> String

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
