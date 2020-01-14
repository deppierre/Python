#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus = ([1 for i in arr if i > 0],[1 for j in arr if j < 0],[1 for k in arr if k == 0])
    print(str(round(sum(plus[0])/len(arr),6))+"\n"+str(round(sum(plus[1])/len(arr),6))+"\n"+str(round(sum(plus[2])/len(arr),6)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)