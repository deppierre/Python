#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    #good method:
    print(str(max([ arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j]  + arr[i+2][j+1] + arr[i+2][j+2] for i in range(4) for j in range(4)])))

    #old method:
    #max_cell_1 = []
    #for i in range(4):
    #    for j in range(4):
            # print(str(arr[i][j]) + " " + str(arr[i][j+1]) + " " + str(arr[i][j+2]))
            # print(" " + str(arr[i+1][j+1]))
            # print(str(arr[i+2][j]) + " " + str(arr[i+2][j+1]) + " " + str(arr[i+2][j+2]))
    #        max_cell_1.append((int(arr[i][j]) + int(arr[i][j+1]) + int(arr[i][j+2]) + int(arr[i+1][j+1]) + int(arr[i+2][j])  + int(arr[i+2][j+1]) + int(arr[i+2][j+2])))

 