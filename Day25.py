def main():
    desiredRow = 2981
    desiredColumn = 3075

    currentValue = 20151125
    number = findNumByCoordinates(desiredRow, desiredColumn)
    for i in range(number-1):
        #print(currentValue)
        currentValue = (currentValue * 252533) % 33554393

    print(f"Number {number} in sequence: {currentValue}")

def findNumByCoordinates(desiredRow, desiredCol):
    #Remember these indices are 1 based
    number = 1

    for i in range(1, desiredRow):
        number += i

    for i in range(1, desiredCol):
        number += i + desiredRow

    return number

if __name__ == "__main__":
    main()