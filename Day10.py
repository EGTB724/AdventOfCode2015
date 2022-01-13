def main():
    inputString = "1113222113"

    for iteration in range(50):
        conCounter = 1
        currentLetter = inputString[0]
        newString = ""
        for index, letter in enumerate(inputString):
            if index == 0:
                continue

            if letter == currentLetter:
                conCounter += 1
            else:
                newString += str(conCounter) + currentLetter
                conCounter = 1
                currentLetter = letter

        newString += str(conCounter) + currentLetter

        print("After " + str(iteration + 1) + " pass: " + newString)

        inputString = newString

    print(len(inputString))



if __name__ == "__main__":
    main()