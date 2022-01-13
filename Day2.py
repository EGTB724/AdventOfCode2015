def main():
    lines = []
    with open('day2.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    dimensions = []
    for line in lines:
        dimensions.append(line.split("x"))

    totalWrap = 0
    totalRibbon = 0
    for dimension in dimensions:
        l1 = int(dimension[0])
        l2 = int(dimension[1])
        l3 = int(dimension[2])

        side1 = int(dimension[0]) * int(dimension[1])
        side2 = int(dimension[1]) * int(dimension[2])
        side3 = int(dimension[2]) * int(dimension[0])

        totalWrap += 2 * (side1 + side2 + side3)
        extraSide = min(side1, side2, side3)
        totalWrap += extraSide

        totalRibbon += 2*l1 + 2*l2 + 2*l3 - 2*max(l1,l2,l3)
        totalRibbon += l1 * l2 * l3




    print(totalWrap)
    print(totalRibbon)


if __name__ == "__main__":
    main()