#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps=0
    my_list=[None for i in range(len(arr)+1)]
    for i in range(len(arr)):
        my_list[arr[i]]=i
    for i in range(len(arr)-1):
        if i!=arr[i]-1:
            arr[i], arr[my_list[i+1]]=arr[my_list[i+1]], arr[i]
            tmp=arr[i]
            tmp_B=arr[my_list[i+1]]
            
            my_list[tmp], my_list[tmp_B] = i, my_list[i+1]
            swaps+=1

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
