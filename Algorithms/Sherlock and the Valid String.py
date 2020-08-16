#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    counter=Counter()
    for ch in s:
        counter[ch]+=1
    ordered=sorted(list(counter.values()))
    if len(ordered)==1:
        return "YES"
    if ordered[0]==1 and ordered[1]==ordered[-1]:
      return "YES"
    start, end = 0, len(ordered)-1
    acceptable_delta=1
    while end-start>0:
        acceptable_delta-=ordered[end]-ordered[start]
        if acceptable_delta<0:
            return "NO"
        start+=1
        end-=1
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
