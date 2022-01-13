import re

def main():
    lines = []
    with open('day5.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    good = 0

    rx1 = re.compile(r'(.)\1{1,}')
    rx2 = re.compile(r'[aeiou].*[aeiou].*[aeiou]')
    for line in lines:
        doubleLetter = rx1.search(line)
        threevowels = rx2.search(line)

        if doubleLetter and threevowels:
            if line.__contains__("ab") or line.__contains__("cd") or line.__contains__("pq") or line.__contains__("xy"):
                continue
            else:
                print(line)
                good += 1

    print("Part 1: " + str(good))
    print()

    secondgood = 0
    rx3 = re.compile(r'(..).*\1')
    rx4 = re.compile(r'(.).\1')
    for line in lines:
        test1 = rx3.search(line)
        test2 = rx4.search(line)

        if test1 and test2:
            secondgood += 1
            print(line)



    print("Part 2: " + str(secondgood))
    print()


if __name__ == "__main__":
    main()