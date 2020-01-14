#!/bin/python3

index = int(input().strip())

listNumbers = list(map(int, input().rstrip().split()))

listNumbers.reverse()

print(' '.join(str(n) for n in listNumbers))