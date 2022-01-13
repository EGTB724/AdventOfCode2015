def main():
    lines = []
    with open('day7.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    instructions = []
    for line in lines:
        instruction = line.split()
        instructions.append(instruction)

    registers = {}
    visited = [False for i in range(len(instructions))]

    while False in visited:
        for index, instruction in enumerate(instructions):
            if "AND" in instruction and visited[index] is False:
                reg1 = instruction[0]
                reg2 = instruction[2]
                output = instruction[4]

                if instruction[0].isnumeric() and reg2 in registers:
                    reg1Num = int(instruction[0])
                    reg2Num = int(registers.get(reg2))
                    outputNum = reg1Num & reg2Num
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

                elif instruction[2].isnumeric() and reg1 in registers:
                    reg1Num = int(registers.get(reg1))
                    reg2Num = int(instruction[2])
                    outputNum = reg1Num & reg2Num
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

                elif reg1 in registers and reg2 in registers:
                    reg1Num = int(registers.get(reg1))
                    reg2Num = int(registers.get(reg2))
                    outputNum = reg1Num & reg2Num
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

            elif "OR" in instruction and visited[index] is False:
                reg1 = instruction[0]
                reg2 = instruction[2]
                output = instruction[4]

                if instruction[0].isnumeric() and reg2 in registers:
                    reg1Num = int(instruction[0])
                    reg2Num = int(registers.get(reg2))
                    outputNum = reg1Num | reg2Num
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

                elif instruction[2].isnumeric() and reg1 in registers:
                    reg1Num = int(registers.get(reg1))
                    reg2Num = int(instruction[2])
                    outputNum = reg1Num | reg2Num
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

                elif reg1 in registers and reg2 in registers:
                    reg1Num = int(registers.get(reg1))
                    reg2Num = int(registers.get(reg2))
                    outputNum = reg1Num | reg2Num
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

            elif "LSHIFT" in instruction and visited[index] is False:
                reg1 = instruction[0]
                shiftValue = int(instruction[2])
                output = instruction[4]

                if reg1 in registers:
                    reg1Num = registers.get(reg1)
                    outputNum = reg1Num << shiftValue
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

            elif "RSHIFT" in instruction and visited[index] is False:
                reg1 = instruction[0]
                shiftValue = int(instruction[2])
                output = instruction[4]

                if reg1 in registers:
                    reg1Num = registers.get(reg1)
                    outputNum = reg1Num >> shiftValue
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

            elif "NOT" in instruction and visited[index] is False:
                reg1 = instruction[1]
                output = instruction[3]

                if reg1 in registers:
                    reg1Num = int(registers.get(reg1))
                    outputNum = ~reg1Num
                    registers[output] = int(outputNum)
                    visited[index] = True
                    print("Visited line " + str(index + 1))

            elif len(instruction) == 3 and visited[index] is False:
                output = instruction[2]

                if instruction[0].isnumeric():
                    registers[output] = int(instruction[0])
                    visited[index] = True
                    print("Visited line " + str(index + 1))

                else:
                    inputReg = instruction[0]
                    if inputReg in registers:
                        outputNum = int(registers.get(inputReg))
                        registers[output] = outputNum
                        visited[index] = True
                        print("Visited line " + str(index + 1))

    print(registers)


if __name__ == "__main__":
     main()