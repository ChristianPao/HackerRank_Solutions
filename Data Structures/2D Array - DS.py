#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    mask=[[-1,-1],[-1,0],[-1,1],[0,0],[1,-1],[1,0],[1,1]]
    best=-9*7
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr)-1):
            h_sum=0
            for e in mask:
                h_sum+=arr[i+e[0]][j+e[1]]
            best=max(best, h_sum)
    return best

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
