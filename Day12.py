def main():
    lines = []
    with open('day12.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    data = lines[0]
    sum = 0
    startObserving = False
    peice = ""
    redZones = []
    openChars = ["{", "["]
    closeChars = ["}", "]"]
    for index, char in enumerate(data):
        if char == "r" and data[index + 1] == "e" and data[index + 2] == "d":
            #Check if its part of an object or an array
            #Backtrack
            lowStack = []
            lowIndex = index
            valid = False
            while(True):
                if data[lowIndex] in closeChars:
                    lowStack.append(data[lowIndex])
                elif data[lowIndex] in openChars:
                    if len(lowStack) == 0:
                        #Check if its a { or [
                        if data[lowIndex] == "{":
                            #Important
                            #Forwardtrack
                            highStack = []
                            highIndex = index
                            while (True):
                                if data[highIndex] in openChars:
                                    highStack.append(data[highIndex])
                                elif data[highIndex] in closeChars:
                                    if len(highStack) == 0:
                                        valid = True
                                        break
                                    else:
                                        highStack.pop()
                                highIndex += 1
                        elif data[lowIndex] == "[":
                            break
                    else:
                        lowStack.pop()
                if valid:
                    break
                lowIndex -= 1

            if valid:
                redZones.append((lowIndex,highIndex))

    print(redZones)

    for index, char in enumerate(data):
        if (char == "-" or char.isnumeric()) and not startObserving and not inRedZone(redZones, index):
            startObserving = True
            peice += char
            continue
        if startObserving:
            if char.isnumeric():
                peice += char
                continue
            else:
                startObserving = False
                print(int(peice))
                sum += int(peice)
                peice = ""

    print(sum)

def inRedZone(redZones, index):
    for zone in redZones:
        low = int(zone[0])
        high = int(zone[1])

        if low <= index <= high:
            return True

    return False

if __name__ == "__main__":
    main()