#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the commonChild function below.
def commonChild(s1, s2):
    set_1=set(list(s1))
    set_2=set(list(s2))
    intersection=set_1.intersection(set_2)
    new_s1="".join([ch for ch in s1 if ch in intersection])
    new_s2="".join([ch for ch in s2 if ch in intersection])
    len_2=len(new_s2)
    prev_line=[0]*len_2
    
    if len_2==0:
        return 0
    curr_line=prev_line.copy()
    for i, ch1 in enumerate(new_s1):
        for j, ch2 in enumerate(new_s2):
            if ch1!=ch2:
                if j==0:
                    curr_line[j]=prev_line[j]
                elif j>0:
                    curr_line[j]=prev_line[j] if prev_line[j]>curr_line[j-1] else curr_line[j-1]
            else:
                if j==0:
                    curr_line[j]=1
                else:
                    curr_line[j]=prev_line[j-1]+1
        prev_line=curr_line.copy()

    return prev_line[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
