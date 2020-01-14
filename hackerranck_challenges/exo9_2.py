#!/bin/python3

if __name__ == '__main__':
    index = int(input().strip())
    listWords = []

    for i in range(index):
        stringInput = input().rstrip()
        listWords.append(stringInput)

    for word in listWords:
        print("".join(stringInput[i] for i in range(len(stringInput)) if i %2 == 0) + " " + "".join(stringInput[i] for i in range(len(stringInput)) if i %2 == 1))