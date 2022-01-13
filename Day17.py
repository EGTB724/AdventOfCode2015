import math
from itertools import combinations

def main():
    lines = []
    with open('day17.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    cups = []
    for line in lines:
        cups.append(int(line))

    binaryString = ["0"] * len(cups)

    desiredSum = 150
    possiblePerms = 0
    perms = []
    for i in range(0, 2**len(cups)):
        #Test binary string
        sum = 0
        for j in range(0, len(cups)):
            sum += int(binaryString[j]) * cups[j]

        if sum == desiredSum:
            possiblePerms += 1
            tmp = [0] * len(cups)
            for j in range(0, len(cups)):
                tmp[j] = int(binaryString[j]) * cups[j]
            perms.append(tmp)

        #Increment binary string
        incrementString(binaryString)

    print(possiblePerms)
    print(perms)

    minContainers = math.inf
    possible = 0
    for perm in perms:
        numContainers = 0
        for i in perm:
            if not i == 0:
                numContainers += 1
        if numContainers == minContainers:
            possible += 1
        if numContainers < minContainers:
            minContainers = numContainers
            possible = 1

    print(minContainers)
    print(possible)




def incrementString(binaryString):
    binaryString.reverse()

    for i in range(0, len(binaryString)):
        if not binaryString[i] == "1":
            binaryString[i] = "1"
            break
        else:
            binaryString[i] = "0"

    return binaryString.reverse()




if __name__ == "__main__":
    main()