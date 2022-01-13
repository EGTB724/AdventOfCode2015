import hashlib

def main():
    inputString = "ckczppom"


    index = 0
    result = ""
    while(True):
        md5String = inputString + str(index)
        result = hashlib.md5(md5String.encode()).hexdigest()

        print(md5String + "       " + result)

        index += 1

        if result[0:6] == "000000":
            break

    print(result)

if __name__ == "__main__":
    main()