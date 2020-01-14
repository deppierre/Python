#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    return int(s)+12

if __name__ == '__main__':
    s = input().split(":")

    if s[2].endswith("AM"): 
        if int(s[0]) == 12: hourMilitary = "00:"
        else: hourMilitary = s[0]+":"
    else: 
        if int(s[0]) == 12: hourMilitary = "12:"
        else: hourMilitary = s[0].replace(s[0],str(int(s[0])+12))+":"

    print(str(hourMilitary)+":".join((i.replace("PM","").replace("AM","") for i in s[1:])))