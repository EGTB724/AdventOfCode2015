def main():
    lines = []
    with open('day23.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    instructions = []
    for line in lines:
        instruction = line.split()
        instructions.append(instruction)

    registers = {}
    registers["a"] = 1
    registers["b"] = 0

    numInstructions = len(instructions)
    index = 0

    while True:
        if index not in range(numInstructions):
            break

        #Get the instruction
        ins = instructions[index]

        #Parse the instruction
        if ins[0] == "hlf":
            registerValue = registers.get(ins[1])
            registers[ins[1]] = int(registerValue / 2)
            index += 1
        elif ins[0] == "tpl":
            registerValue = registers.get(ins[1])
            registers[ins[1]] = registerValue * 3
            index += 1
        elif ins[0] == "inc":
            registerValue = registers.get(ins[1])
            registers[ins[1]] = registerValue + 1
            index += 1
        elif ins[0] == "jmp":
            index += int(ins[1])
        elif ins[0] == "jie":
            registerValue = registers.get(ins[1][0])
            if registerValue % 2 == 0:
                index += int(ins[2])
            else:
                index += 1
        elif ins[0] == "jio":
            registerValue = registers.get(ins[1][0])
            if registerValue == 1:
                index += int(ins[2])
            else:
                index += 1


    print(registers)

if __name__ == "__main__":
     main()