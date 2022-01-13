def main():
    lines = []
    with open('day1.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    floor = 0
    for index, letter in enumerate(lines[0]):
        if letter == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print(index + 1)
            quit(1)

    print(floor)

if __name__ == "__main__":
    main()