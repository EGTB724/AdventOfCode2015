import re

def main():
    lines = []
    with open('day19.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    conversions = []
    inputString = ""
    for index, line in enumerate(lines):
        if line == "":
            inputString = lines[index + 1]
            break

        tmp = line.split()
        conversion = (tmp[0],tmp[2])
        conversions.append(conversion)


    #Split the input string by capital letters
    splitInput = re.findall('[A-Z][^A-Z]*', inputString)

    possibilities = []
    for index, element in enumerate(splitInput):
        for conversion in conversions:
            if element == conversion[0]:
                tmp = copyList(splitInput)
                tmp[index] = conversion[1]
                possibilities.append(''.join(tmp))


    uniquePossibilities = []
    for item in possibilities:
        if not item in uniquePossibilities:
            uniquePossibilities.append(item)

    print(len(uniquePossibilities))

    target = inputString
    notDone = True
    step = 0
    while(notDone):
        possibleConversions = []
        yep = []
        for start, end in conversions:
            if end in target:
                possibleConversions.append(end)
                yep.append(start)

        if len(possibleConversions) == 0:
            quit(1)

        longestConversionLength = 0
        bindex = 0
        longestConversion = ""
        for index, item in enumerate(possibleConversions):
            if len(item) > longestConversionLength:
                longestConversionLength = len(item)
                longestConversion = item
                bindex = index

        target = target.replace(longestConversion, yep[bindex], 1)
        step += 1

        if target == "E":
            break

    print(step)

def copyList(list):
    tmp = []
    for item in list:
        tmp.append(item)
    return tmp

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)


if __name__ == "__main__":
    main()