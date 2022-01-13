import math

def main():
    #The hero has 50 hp
    hero = Player(50, 0, 0, 500)

    #Enemy is based on puzzle input
    enemy = Player(51, 9, 0, 0)


    shield = 0
    poison = 0
    recharge = 0
    round = 0
    manaSpent = 0

    #Simulate starting the game with the five different attack types
    print("Starting 1st iteration")
    mmstart = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "MM", round, shield, poison, recharge, manaSpent, math.inf)

    print("Starting 2nd iteration")
    dstart = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "D", round, shield, poison, recharge, manaSpent, mmstart)

    print("Starting 3rd iteration")
    sstart = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "S", round, shield, poison, recharge, manaSpent, min(mmstart, dstart))

    print("Starting 4th iteration")
    pstart = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "P", round, shield, poison, recharge, manaSpent, min(mmstart, dstart, sstart))

    print("Starting 5th iteration")
    rstart = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "R", round, shield, poison, recharge, manaSpent, min(mmstart, dstart, sstart, pstart))

    print(min(mmstart, dstart, sstart, pstart, rstart))

def playRound(hero, enemy, attack, round, shield, poison, recharge, manaSpent, lowest):
    if manaSpent > lowest:
        print("Spent mana is too high, ending game")
        return math.inf

    # Hard mode, player takes one hitpoint per turn
    hero.hitpoints = hero.hitpoints - 1
    if hero.hitpoints <= 0:
        print("Hero dies, game discarded")
        return math.inf

    # Check for effects
    if shield > 0:
        # We lost our shield effect
        hero.armor = 7
        shield -= 1

    if poison > 0:
        # Poison active, deal three damage to boss
        enemy.hitpoints = enemy.hitpoints - 3
        poison -= 1

    if recharge > 0:
        # Recharge active, give hero mana
        hero.mana = hero.mana + 101
        recharge -= 1

    #Check for the attack used by the hero
    if attack == "MM":
        #Check if hero has enough mana
        if hero.mana >= 53:
            print("Player uses Magic Missile")
            #Hero plays magic missle, does 4 damage to enemy
            hero.mana = hero.mana - 53
            manaSpent += 53
            enemy.hitpoints = enemy.hitpoints - 4
        else:
            #End this line of the tree
            return math.inf

    if attack == "D":
        #Check if hero has enough mana
        if hero.mana >= 73:
            print("Player uses Drain")
            #Hero plays drain, it does 2 damage to enemy and heals hero 2 hitpoints
            hero.mana = hero.mana - 73
            manaSpent += 73
            enemy.hitpoints = enemy.hitpoints - 2
            hero.hitpoints = hero.hitpoints + 2
        else:
            #End this line of the tree
            return math.inf

    if attack == "S":
        #Check if hero has enough mana
        if hero.mana >= 113:
            if shield == 0:
                print("Player uses Shield")
                #Hero plays shield, it increases armor by 7 for 6 turns
                hero.mana = hero.mana - 113
                manaSpent += 113

                #Effects start on the next turn
                shield = 6
            else:
                print("Cannot cast effect when it's already in play")
                return math.inf
        else:
            #End this line of the tree
            return math.inf

    if attack == "P":
        if hero.mana >= 173:
            if poison == 0:
                print("Player uses Poison")
                #Hero plays poison, it decreases enemy health by 3 each round for 6 rounds
                hero.mana = hero.mana - 173
                manaSpent += 173

                #Effects start on the next turn
                poison = 6
            else:
                print("Cannot cast effect when it's already in play")
                return math.inf
        else:
            #End this line of the tree
            return math.inf

    if attack == "R":
        if hero.mana >= 229:
            if recharge == 0:
                print("Player uses Recharge")
                #Hero plays recharge, it gives hero 101 mana each round for 5 rounds
                hero.mana = hero.mana - 229
                manaSpent += 229

                #Effects start on the turn
                recharge = 5
            else:
                print("Cannot cast effect when it's already in play")
                return math.inf
        else:
            #End this line of the tree
            return math.inf

    #See if hero or enemy is dead
    if enemy.hitpoints <= 0:
        print("Hero wins, mana used: " + str(manaSpent))
        return manaSpent


    # Check for effects
    if shield > 0:
        # We lost our shield effect
        hero.armor = 7
        shield -= 1

    if poison > 0:
        # Poison active, deal three damage to boss
        enemy.hitpoints = enemy.hitpoints - 3
        poison -= 1

    if recharge > 0:
        # Recharge active, give hero mana
        hero.mana = hero.mana + 101
        recharge -= 1

    #Simulate the enemy attack
    enemyAttack = enemy.damage - hero.armor
    if enemyAttack <= 0:
        enemyAttack = 1
    hero.hitpoints = hero.hitpoints - enemyAttack

    # See if hero or enemy is dead
    if hero.hitpoints <= 0:
        print("Hero dies, game discarded")
        return math.inf


    # Simulate starting the game with the five different attack types
    a = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "MM", round, shield, poison, recharge, manaSpent, lowest)
    b = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "D", round, shield, poison, recharge, manaSpent, min(lowest,a))
    c = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "S", round, shield, poison, recharge, manaSpent, min(lowest,a,b))
    d = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "P", round, shield, poison, recharge, manaSpent, min(lowest,a,b,c))
    e = playRound(deepCopyPlayer(hero), deepCopyPlayer(enemy), "R", round, shield, poison, recharge, manaSpent, min(lowest,a,b,c,d))
    return min(a, b, c, d, e)

def deepCopyPlayer(player):
    return(Player(player.hitpoints, player.damage, player.armor, player.mana))

def deepCopyList(list):
    tmp = [False for i in range(len(list))]
    for i in range(0, len(list)):
        tmp[i] = list[i]
    return tmp

class Player:
    def __init__(self, hitpoints, damage, armor, mana):
        self.hitpoints = hitpoints
        self.damage = damage
        self.armor = armor
        self.mana = mana


if __name__ == "__main__":
    main()