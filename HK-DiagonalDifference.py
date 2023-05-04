#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primaryDiagonal = 0
    secondaryDiagonal = 0

    for i in range(0, len(arr)):
         primaryDiagonal =  primaryDiagonal + arr[i][i]
    for j in range(0,len(arr)):
         secondaryDiagonal = secondaryDiagonal + arr[j][len(arr)-1-j]
    print(abs( primaryDiagonal - secondaryDiagonal))


       

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
