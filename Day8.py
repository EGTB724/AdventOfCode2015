def main():
    lines = []
    with open('day8.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    codeChars = 0
    memChars = 0
    ogChars = 0
    for line in lines:
        lineMemChars = 0
        lineCodeChars = 0
        lineCodeChars += len(line)
        codeChars += len(line)
        ogChars += len(line)
        skipIndex = [False for i in range(len(line))]
        for index, char in enumerate(line):
            if skipIndex[index]:
                continue
            if char == "\"":
                codeChars += 2
                lineCodeChars += 2
                continue
            elif char == "\\":
                if line[index+1] == "x":
                    skipIndex[index + 1] = True
                    skipIndex[index + 2] = True
                    skipIndex[index + 3] = True
                    memChars += 1
                    lineMemChars += 1
                    codeChars += 1
                    lineCodeChars += 1
                elif line[index+1] == "\\":
                    skipIndex[index + 1] = True
                    memChars += 1
                    lineMemChars += 1
                    codeChars += 2
                    lineCodeChars += 2
                else:
                    skipIndex[index + 1] = True
                    memChars += 1
                    lineMemChars += 1
                    codeChars += 2
                    lineCodeChars += 2
            else:
                memChars += 1
                lineMemChars += 1

        print(line + " has " + str(lineCodeChars) + " actual characters")
        print(line + " has " + str(lineMemChars) + " characters in memory")

    print("Total characters: " + str(codeChars))
    #print("Actual characters in memory: " + str(memChars))
    print(ogChars)
    print("Total - Memory: " + str(codeChars - ogChars))


if __name__ == "__main__":
    main()