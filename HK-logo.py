import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    z = Counter(sorted(s))
    # print(z)
    mc = z.most_common(3)
    # print(mc)
    for i in mc:
        print(*i)