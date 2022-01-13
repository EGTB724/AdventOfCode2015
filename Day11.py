import re

def main():
    inputString = "hxbxwxba"
    inputList = list(inputString)

    rx1 = re.compile(r'(.)\1.*(.)\2')
    rx2 = re.compile(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz')

    firstTime = True
    while(True):
        inputList = incrementPassword(inputList)

        testString = ''.join(inputList)
        print(testString)

        test1 = rx1.search(testString)
        test2 = rx2.search(testString)

        if test1 and test2:
            if "i" in testString or "l" in testString or "o" in testString:
                continue
            else:
                if firstTime:
                    firstTime = False
                    firstAnswer = testString
                else:
                    secondAnswer = testString
                    break

    print("First password: " + firstAnswer)
    print("Second password: " + secondAnswer)


def incrementPassword(inputList):
    inputList.reverse()
    for index, char in enumerate(inputList):
        if not char == "z":
            inputList[index] = chr(ord(char) + 1)
            break
        else:
            inputList[index] = "a"
    inputList.reverse()
    return inputList

if __name__ == "__main__":
    main()