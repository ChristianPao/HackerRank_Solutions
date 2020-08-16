#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    pivot_indexes=set([tup[0] for tup in queries]).union(set([tup[1] for tup in queries]))
    pivot_indexes=sorted(list(pivot_indexes))
    starts={}
    ends={}
    for pivot in pivot_indexes:
        starts[pivot]=0
        ends[pivot]=0
    for q in queries:
        starts[q[0]]=starts.get(q[0])+q[2]
        ends[q[1]]=ends.get(q[1])-q[2]
    flow=0
    maximum=0
    for i in pivot_indexes:

        if maximum<flow+starts[i]:
            maximum=flow+starts[i]
        flow+=starts[i]+ends[i]
            
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
