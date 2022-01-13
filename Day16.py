def main():
    lines = []
    with open('day16.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    knownAunt = Aunt()
    knownAunt.children = 3
    knownAunt.cats = 7
    knownAunt.samoyeds = 2
    knownAunt.pomeranians = 3
    knownAunt.akitas = 0
    knownAunt.vizslas = 0
    knownAunt.goldfish = 5
    knownAunt.trees = 3
    knownAunt.cars = 2
    knownAunt.perfumes = 1

    aunts = []
    for numAunt, line in enumerate(lines):
        aunt = Aunt()
        tmp = line.split()
        for index, item in enumerate(tmp):
            aunt.number = numAunt + 1
            if item[:-1] == "children":
                aunt.children = int(tmp[index + 1])
            if item[:-1] == "cats":
                aunt.cats = int(tmp[index + 1])
            if item[:-1] == "samoyeds":
                aunt.samoyeds = int(tmp[index + 1])
            if item[:-1] == "pomeranians":
                aunt.pomeranians = int(tmp[index + 1])
            if item[:-1] == "akitas":
                aunt.akitas = int(tmp[index + 1])
            if item[:-1] == "vizslas":
                aunt.vizslas = int(tmp[index + 1])
            if item[:-1] == "goldfish":
                aunt.goldfish = int(tmp[index + 1])
            if item[:-1] == "trees":
                aunt.trees = int(tmp[index + 1])
            if item[:-1] == "cars":
                aunt.cars = int(tmp[index + 1])
            if item[:-1] == "perfumes":
                aunt.perfumes = int(tmp[index + 1])
        aunts.append(aunt)

        possibleAunts = []
        for aunt in aunts:
            potentialMatch = True

            if aunt.children is not None:
                if not aunt.children == knownAunt.children:
                    potentialMatch = False
            if aunt.cats is not None:
                if not aunt.cats > knownAunt.cats:
                    potentialMatch = False
            if aunt.samoyeds is not None:
                if not aunt.samoyeds == knownAunt.samoyeds:
                    potentialMatch = False
            if aunt.pomeranians is not None:
                if not aunt.pomeranians < knownAunt.pomeranians:
                    potentialMatch = False
            if aunt.akitas is not None:
                if not aunt.akitas == knownAunt.akitas:
                    potentialMatch = False
            if aunt.vizslas is not None:
                if not aunt.vizslas == knownAunt.vizslas:
                    potentialMatch = False
            if aunt.goldfish is not None:
                if not aunt.goldfish < knownAunt.goldfish:
                    potentialMatch = False
            if aunt.trees is not None:
                if not aunt.trees > knownAunt.trees:
                    potentialMatch = False
            if aunt.cars is not None:
                if not aunt.cars == knownAunt.cars:
                    potentialMatch = False
            if aunt.perfumes is not None:
                if not aunt.perfumes == knownAunt.perfumes:
                    potentialMatch = False

            if potentialMatch:
                possibleAunts.append(aunt)



    for aunt in possibleAunts:
        print(aunt.number)



class Aunt:
    def __init__(self):
        self.number = None
        self.children = None
        self.cats = None
        self.samoyeds = None
        self. pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None

if __name__ == "__main__":
    main()


