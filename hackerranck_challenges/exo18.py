
#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    return [i + ( 5 - i % 5) if i > 35 and i %5 >=3 else i for i in grades]

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    for x in gradingStudents(grades):
        print(x)



#73
#67
#38
#33