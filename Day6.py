import numpy as np

def main():
    lines = []
    with open('day6.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    instructions = []
    for line in lines:
        instruction = []
        tmp = line.split()

        if tmp[0] == "toggle":
            instruction.append(tmp[0])

            tmpnum = tmp[1].split(",")
            instruction.append(int(tmpnum[0]))
            instruction.append(int(tmpnum[1]))

            tmpnum = tmp[3].split(",")
            instruction.append(int(tmpnum[0]))
            instruction.append(int(tmpnum[1]))

            instructions.append(instruction)
        elif tmp[0] == "turn":
            instruction.append(tmp[1])

            tmpnum = tmp[2].split(",")
            instruction.append(int(tmpnum[0]))
            instruction.append(int(tmpnum[1]))

            tmpnum = tmp[4].split(",")
            instruction.append(int(tmpnum[0]))
            instruction.append(int(tmpnum[1]))

            instructions.append(instruction)

    lights = np.zeros((1000,1000), dtype=np.int_)

    for instruction in instructions:
        minX = min(instruction[2], instruction[4])
        maxX = max(instruction[2], instruction[4])
        minY = min(instruction[1], instruction[3])
        maxY = max(instruction[1], instruction[3])
        if instruction[0] == "on":
            for i in range(minY, maxY + 1):
                for j in range(minX, maxX + 1):
                    lights[i][j] += 1
        elif instruction[0] == "off":
            for i in range(minY, maxY + 1):
                for j in range(minX, maxX + 1):
                    if not lights[i][j] == 0:
                        lights[i][j] -= 1
        elif instruction[0] == "toggle":
            for i in range(minY, maxY + 1):
                for j in range(minX, maxX + 1):
                    lights[i][j] += 2

    numOnes = np.sum(lights)
    print(numOnes)

if __name__ == "__main__":
    main()