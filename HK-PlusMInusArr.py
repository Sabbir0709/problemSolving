#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    m = len(arr)
    for i in range(0, len(arr)):
        if(arr[i] < 0):
            n = n + 1
        if(arr[i] > 0):
            p = p + 1
        elif(arr[i] == 0):
            z = z + 1
        else:
            continue
    print(p/m)
    print(n/m)
    print(z/m)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
