def main():
    lines = []
    with open('day15.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    ingredients = []
    for line in lines:
        tmp = line.split()
        capacity = int(tmp[2][:-1])
        durability = int(tmp[4][:-1])
        flavor = int(tmp[6][:-1])
        texture = int(tmp[8][:-1])
        calories = int(tmp[10])
        ingredients.append(Ingredient(capacity, durability, flavor, texture, calories))

    highScore = 0
    for sprinkles in range(1, 101):
        for peanutButter in range(1, 101):
            for frosting in range(1, 101):
                for sugar in range(1, 101):
                    if sprinkles + peanutButter + frosting + sugar == 100:

                        calories = sprinkles * ingredients[0].calories + peanutButter * ingredients[1].calories + frosting * ingredients[2].calories + sugar * ingredients[3].calories

                        if not calories == 500:
                            continue

                        print("Sprinkles: {}  PB: {}  Frosting: {}  Sugar: {}  Calories: {}".format(sprinkles, peanutButter, frosting, sugar, calories))

                        capacity = sprinkles * ingredients[0].capacity + peanutButter * ingredients[1].capacity + frosting * ingredients[2].capacity + sugar * ingredients[3].capacity

                        durability = sprinkles * ingredients[0].durability + peanutButter * ingredients[1].durability + frosting * ingredients[2].durability + sugar * ingredients[3].durability

                        flavor = sprinkles * ingredients[0].flavor + peanutButter * ingredients[1].flavor + frosting * ingredients[2].flavor + sugar * ingredients[3].flavor

                        texture = sprinkles * ingredients[0].texture + peanutButter * ingredients[1].texture + frosting * ingredients[2].texture + sugar * ingredients[3].texture

                        if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
                            continue
                        else:
                            score = capacity * durability * flavor * texture


                        if score > highScore:
                            highScore = score

    print(highScore)



class Ingredient:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories



if __name__ == "__main__":
    main()