#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max = candles[0]
    count = 0
    arr = []
    for i in range(1, len(candles)):
        if candles[i] > max:
            max = candles[i]
            # arr.append(max)
    for i in range(0, len(candles)):
        if max == candles[i]:
            count = count+1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
