#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    indexes={}
    total_counter=0
    for i, e in enumerate(arr):
        indexes[e]=indexes.get(e, [])
        indexes[e].append(i)
    print(indexes)
    for key in indexes.keys():
        list_i=indexes.get(key, [])
        if len(list_i)==0:
            continue
        list_j=indexes.get(key*r, [])
        if len(list_j)==0:
            continue
        list_k=indexes.get(key*r*r, [])
        if len(list_k)==0:
            continue
        i, j, k=len(list_i)-1, len(list_j)-1, len(list_k)-1
        counter_a, counter_b, counter_c=0,0,0
        # bring to valid initial state
        changed=True
        while changed:
            changed=False
            if list_k[k]<=list_j[j]:#j needs to move back
                if list_j[j]<=list_i[i]:#also i
                    j-=1
                    i-=1
                    changed=True
                else:
                    j-=1
                    changed=True
            if list_j[j]<=list_i[i]:
                i-=1
                changed=True
        if list_i[i]<list_j[j]<list_k[k]:
            counter_c+=1
        else:
            continue
        while i>=0:
            if list_k[k-1]<=list_j[j] or k==0:#then we need to move back j
                if list_j[j-1]<=list_i[i] or j==0:#then we need to move back i too
                    i-=1
                    if list_i[i]<list_j[j]<list_k[k] and i>=0:
                        counter_a+=counter_b+counter_c
                else:
                    j-=1
                    if list_i[i]<list_j[j]<list_k[k]:
                        counter_b+=counter_c
            else:
                k-=1
                counter_c+=1
            
        total_counter+=counter_a+counter_b+counter_c
    return total_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
