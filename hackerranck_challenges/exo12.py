#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    #Solution1:
    #for j in range(1,n+1): print("".join([" " for i in range(n-j)]+["#" for i in range(j)]))

    #Soluton 2:
    for j in range(1,n+1): print(" " * (n-j) + ("#" * j) )

if __name__ == '__main__':
    n = int(input())

    staircase(n)
