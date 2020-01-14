#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    result = []
    
    for i in range(len(arr)): result.append(sum(arr) - arr[i])

    print(str(min(result)) + " " + str(max(result)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
