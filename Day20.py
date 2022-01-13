import math

def main():
    input = 36000000

    house = 7
    while True:
        score = 0
        for i in range(1, int(math.sqrt(house))+1):
            if house % i == 0:
                if house / i == i:
                    if not house > i * 50:
                        score += i
                else:
                    if not house > i * 50:
                        score += i
                    if not house > int(house/i) * 50:
                        score += int(house / i)
        score *= 11
        print("House " + str(house) + ": " + str(score))

        if score >= input:
           break

        house += 1

if __name__ == "__main__":
    main()