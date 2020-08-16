#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q=list(map(lambda x:x-1, q))
    bribes=0
   
    for i in range(len(q)-1, -1, -1):
        if q[i]-i>2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i]-1), i):
            if q[j]>q[i]:
                bribes+=1
        
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
