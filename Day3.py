def main():
    lines = []
    with open('day3.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    santaCoordinates = []
    roboCoordinates = []

    santaCoordinates.append((0,0))
    roboCoordinates.append((0,0))

    santaX = 0
    santaY = 0
    robotX = 0
    robotY = 0
    for index, letter in enumerate(lines[0]):
        if index%2 == 0:
            if letter == ">":
                santaX += 1
            if letter == "<":
                santaX -= 1
            if letter == "^":
                santaY += 1
            if letter == "v":
                santaY -= 1
            santaCoordinates.append((santaX, santaY))
        if index%2 == 1:
            if letter == ">":
                robotX += 1
            if letter == "<":
                robotX -= 1
            if letter == "^":
                robotY += 1
            if letter == "v":
                robotY -= 1
            roboCoordinates.append((robotX, robotY))

    nonDup = []
    for coordinate in santaCoordinates:
        if not coordinate in nonDup:
            nonDup.append(coordinate)
    for coordinate in roboCoordinates:
        if not coordinate in nonDup:
            nonDup.append(coordinate)


    print(len(nonDup))

if __name__ == "__main__":
    main()