#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] < 38:
          print(grades[i])
        elif grades[i] % 5 == 3:
            grades[i] = grades[i]+2
            print(grades[i])
        elif grades[i] % 5 == 4:
            grades[i] = grades[i]+1
            print(grades[i])  
        else:
            print(grades[i])
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())
    grades = []

    for _ in range(0,grades_count):
        item = int(input().strip())
        grades.append(item)

    gradingStudents(grades)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
