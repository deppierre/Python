#!/bin/python3

index = int(input().strip())

listNumbers = list(map(str, input().rstrip().split()))

#solution 1
revertList1 = ""
for i in range(1,len(listNumbers)+1):
    revertList1 += listNumbers[-i]+ " "

#solution 2
revertList2 = " ".join(listNumbers[-i] for i in range(1,len(listNumbers)+1))

print(revertList1)
print(revertList2)