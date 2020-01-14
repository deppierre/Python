#!/bin/python3

import math
import os
import random
import re
import sys


def multiplicator(number):
    if number >= 2 and number <= 20:
        for i in range(1,11):
            print(str(number)+" x "+str(i)+" = "+str(i * number))

if __name__ == '__main__':
    n = int(input())
    multiplicator(n)