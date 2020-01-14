#!/bin/python3

import math
import os
import random
import re
import sys


def getbinary(n):
    while n > 0:
        remainder.append(n%2)
        n = int(n/2)

    maxValue = 0
    tempMaxValue = 0

    for i in range(len(remainder)):
        if tempMaxValue > maxValue: maxValue = tempMaxValue 
        tempMaxValue = 0

        while remainder[i] == 1: 
            tempMaxValue += 1
            if i < len(remainder) - 1: i += 1
            else: break

    print(str(maxValue))

    
if __name__ == '__main__':
    remainder = []
    n = int(input())

    getbinary(n)
