#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps=0
    pointer=0
    while pointer<len(c)-2:
        if c[pointer+2]==1:
            pointer+=1
        else:
            pointer+=2
        jumps+=1
    return jumps if pointer==len(c)-1 else jumps+1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
