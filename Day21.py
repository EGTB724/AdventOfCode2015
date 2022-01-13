from itertools import combinations
import math

def main():
    # Instantiate the shop, this is predetermined
    weapons = []
    armor = []
    rings = []

    weapons.append(Weapon("Dagger", 8, 4))
    weapons.append(Weapon("Shortsword", 10, 5))
    weapons.append(Weapon("Warhammer", 25, 6))
    weapons.append(Weapon("Longsword", 40, 7))
    weapons.append(Weapon("Greataxe", 74, 8))

    armor.append(Armor("Leather", 13, 1))
    armor.append(Armor("Chainmail", 31, 2))
    armor.append(Armor("Splintmail", 53, 3))
    armor.append(Armor("Bandemail", 75, 4))
    armor.append(Armor("Platemail", 102, 5))

    rings.append(Ring("Damage +1", 25, 1, 0))
    rings.append(Ring("Damage +2", 50, 2, 0))
    rings.append(Ring("Damage +3", 100, 3, 0))
    rings.append(Ring("Defense +1", 20, 0, 1))
    rings.append(Ring("Defense +2", 40, 0, 2))
    rings.append(Ring("Defense +3", 80, 0, 3))

    lines = []
    with open('day21.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    variants = [(1,0,0),(1,0,1),(1,0,2),(1,1,0),(1,1,1),(1,1,2)]

    arsenals = []
    for variant in variants:
        numWeapons = variant[0]
        numArmor = variant[1]
        numRings = variant[2]

        weaponV = list(combinations(weapons, numWeapons))
        armorV = list(combinations(armor, numArmor))
        ringV = list(combinations(rings, numRings))

        for weapont in weaponV:
            for armort in armorV:
                for ringt in ringV:
                    arsenalList = weapont + armort + ringt
                    arsenals.append(arsenalList)


    enemy = Player(100, 8, 2)

    lowestCost = math.inf
    highestCost = 0

    for arsenal in arsenals:
        heroHealth = 100
        heroDamage = 0
        heroArmor = 0
        cost = 0
        for item in arsenal:
            if isinstance(item, Weapon):
                heroDamage += item.damage
            if isinstance(item, Armor):
                heroArmor += item.armor
            if isinstance(item, Ring):
                heroDamage += item.damage
                heroArmor += item.armor
            cost += item.cost

        hero = Player(heroHealth, heroDamage, heroArmor)
        result = playGame(hero, enemy)
        print(result)

        if result == "Won":
            if cost < lowestCost:
                lowestCost = cost

        if result == "Loss":
            if cost > highestCost:
                highestCost = cost

    print("Lowest cost to Win Game: " + str(lowestCost))
    print("Highest cost to Lose Game: " + str(highestCost))



def playGame(hero, enemy):
    heroAttack = hero.damage - enemy.armor
    if heroAttack < 1:
        heroAttack = 1

    enemyAttack = enemy.damage - hero.armor
    if enemyAttack < 1:
        enemyAttack = 1

    if heroAttack >= enemyAttack:
        return "Won"
    else:
        return "Loss"


class Player:
    def __init__(self, hitpoints, damage, armor):
        self.hitpoints = hitpoints
        self.damage = damage
        self.armor = armor

class Weapon:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage

class Armor:
    def __init__(self, name, cost, armor):
        self.name = name
        self.cost = cost
        self.armor = armor

class Ring:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor




if __name__ == "__main__":
    main()