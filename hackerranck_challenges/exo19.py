#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_over_the_house = [1 for i in apples if s - (a + i) <= 0 and (a + i) <= t]
    oranges_over_the_house = [1 for i in oranges if (b + i) <= t and (b + i) >= s]

    print(str(sum(apples_over_the_house)) + "\n" + str(sum(oranges_over_the_house)))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
