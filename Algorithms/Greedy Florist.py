#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c, n):
    c=sorted(c, reverse=True)
    flower_i=0
    mul_const=1
    person_i=0
    tot=0
    remaining_flowers=n
    while remaining_flowers>0:
        tot+=mul_const*c[flower_i]
        remaining_flowers-=1
        flower_i+=1
        person_i+=1
        if person_i==k:
            person_i=0
            mul_const+=1
    return tot


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c, n)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
