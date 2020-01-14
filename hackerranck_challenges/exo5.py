#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
# 5 6 7
# 3 6 10
def compareTriplets(a, b):
    alice, bob, i = 0, 0, 0
    while i <= len(a) - 1:
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        i += 1
    return bob, alice


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(str(result))

    if os.environ['OS'].lower() != "WINDOWS_NT".lower():
        fptr = open(os.environ['PUBLIC'], 'w')
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

        fptr.close()
