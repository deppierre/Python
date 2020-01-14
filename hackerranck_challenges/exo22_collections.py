#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the migratoryBirds function below.

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    spot = collections.Counter(arr)
    print(spot.most_common(1)[0][0])
    print("END")