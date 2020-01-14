#!/bin/python3

def evenOdd(stringInput):
    stringOutputEven = stringOutputOdd = ""
    for i in range(len(stringInput)):
        if(i %2) == 0:
            stringOutputEven += stringInput[i]
        else:
            stringOutputOdd += stringInput[i]
    
    return stringOutputEven + " " + stringOutputOdd

if __name__ == '__main__':
    index = int(input().strip())
    listWords = []

    for i in range(index):
        stringInput = input().rstrip()
        listWords.append(stringInput)

    for word in listWords:
        print(evenOdd(word))