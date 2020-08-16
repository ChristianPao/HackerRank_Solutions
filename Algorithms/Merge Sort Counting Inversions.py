#!/bin/python3

import math
import os
import random
import re
import sys


def merge_sort(arr, len_arr): 
    swaps=0
    if len_arr >1: 
        mid = len_arr//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        swaps_l=merge_sort(L, mid) # Sorting the first half 
        swaps_r=merge_sort(R, len_arr-mid) # Sorting the second half 
        i = j = k = 0
        len_L=mid
        len_R=len_arr-mid
        # Copy data to temp arrays L[] and R[] 
        while i < len_L and j < len_R:
            if L[i] <= R[j]: 
                arr[k] = L[i]
                i+=1
            else:
                swaps+=len_L-i
                arr[k] = R[j]
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len_L: 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len_R: 
            arr[k] = R[j] 
            j+=1
            k+=1
        swaps+=swaps_l+swaps_r
    return swaps

# Complete the countInversions function below.
def countInversions(arr):
    swaps=merge_sort(arr, len(arr))
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
