#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
# Unsolveddddddddddddddd!!!
def divisibleSumPairs(n, k, ar):
    count = 0
    list = []
    for i in range(0, n):
        for j in range(1,n):
            if i<j:
                sum = ar[i] + ar[j]
                if sum%k == 0:
                    list.append(sum)
                    count += 1
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list)
    print(list)
   


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
  
