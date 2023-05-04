import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    start = 1
    end = n
    search = p
    count1 = 0
    count2 = 0
    
    if (start == search):
       return count1
    
    if (end % 2 == 0  and end == search):
        return count2
    
    if (end % 2 != 0):
        if(search in range(end-1,end)):
            return count2

    
    while (start != search):
        start = start + 2
        count1 = count1 + 1
        if(search in range(start-1,start)):
            break

    while (end != search):

        if(end % 2 == 0):
            end = end -1
            count2 = count2 + 1
            if(search in range(end-1,end)):
                break


        if(end % 2 != 0):
            end = end - 2
            count2 = count2 + 1
            if(search in range(end-1,end)):
                break

    if(count1 < count2):
        return count1
    else:
        return count2
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()