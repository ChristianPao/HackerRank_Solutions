#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

def median_given_sorted(arr):
    if len(arr)%2>0:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2-1]+arr[len(arr)//2])/2

def median_given_sorted(arr):
    if len(arr)%2>0:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2-1]+arr[len(arr)//2])/2

def binary_search (arr, l, r, x, insertion): 
    try:
        if r >= l: 
            mid = l + (r - l)//2
            
            if insertion and arr[max(mid-1, 0)]<=x<=arr[mid]: 
                return mid
            elif not insertion and arr[mid]==x:
                return mid
            elif arr[mid] > x: 
                return binary_search(arr, l, mid-1, x, insertion) 
            else: 
                return binary_search(arr, mid + 1, r, x, insertion) 
        else: 
            return "asdlfj"
    except Exception:
        print("arr:",arr, "L:",l, "R:",r, "X:",x)

def insert_in_sort(queue, new_number):
    if new_number<=queue[0]:
        queue.appendleft(new_number)
    elif new_number>=queue[-1]:
        queue.append(new_number)
    else:
        queue.insert(binary_search(queue, 0, len(queue), new_number, insertion=True), new_number)
        

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    #queue only used to calculate median
    queue=deque(sorted(expenditure[:d]))
    counts=0
    for i in range(d, len(expenditure)):
        m=median_given_sorted(queue)
        if m*2<=expenditure[i]:
            counts+=1
        del queue[binary_search(queue, 0, len(queue), expenditure[i-d], insertion=False)]
        insert_in_sort(queue, expenditure[i])
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
