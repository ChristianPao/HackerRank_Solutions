#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr=sorted(arr)
    min_delta=10**9
    for i in range(len(arr)-k+1):
        curr_min=arr[i]
        curr_max=arr[i+k-1]
        if curr_max-curr_min<min_delta:
            min_delta=curr_max-curr_min
    return min_delta

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
