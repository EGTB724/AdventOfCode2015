from itertools import combinations
import math

def main():
    lines = []
    with open('day24.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    weights = []
    totalWeight = 0
    for line in lines:
        weights.append(int(line))
        totalWeight += int(line)

    groupWeight = int(totalWeight / 4)

    print(groupWeight)

    bestEntanglement = math.inf
    for i in range(1, len(weights)):
        for perm in combinations(weights, i):
            if sum(perm) == groupWeight:
                bestEntanglement = min(math.prod(perm), bestEntanglement)

    print(bestEntanglement)

if __name__ == "__main__":
    main()



