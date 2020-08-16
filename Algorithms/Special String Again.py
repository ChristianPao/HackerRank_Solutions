#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    upper_bound=0
    n_valid=n
    # Find groups of equals
    while upper_bound<n-1:
        group_dim=0
        while upper_bound<n-1 and s[upper_bound+1]==s[upper_bound]:
            group_dim+=1
            upper_bound+=1
        n_valid+=group_dim*(group_dim+1)/2
        upper_bound+=1

    # Find all equal except middle substr
    for middle in range(1, n-1):
        lb, ub = middle-1, middle+1
        if s[middle]!=s[lb]:
            while lb>=0 and ub<=n-1 and s[lb]==s[ub]:
                n_valid+=1
                lb-=1
                ub+=1
                # Ensure that not only ub and lb are equal
                if lb>=0 and s[lb]!=s[lb+1]:
                    break
    return int(n_valid)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
