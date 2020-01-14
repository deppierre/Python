#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
# lidee cest quon doit rester dans la boucle jusqua trouver la base (n > 1), sinon on retourne le resultat
def factorial(n):
    if n > 1: return n * factorial(n - 1)
    else: return n

if __name__ == '__main__':
    n = int(input())

    result = factorial(n)

    print(result)