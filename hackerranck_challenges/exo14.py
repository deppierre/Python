#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar): 
    return ar.count(max(ar))

if __name__ == '__main__':

    ar_count = int(input())
 
    #file = open("C:\\Users\\pdepretz\\Documents\\temp")
    #ar = list(file.read().split())

    ar = list(map(int, input().rstrip().split()))

    print(birthdayCakeCandles(ar))