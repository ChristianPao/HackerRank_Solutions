#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    counter={}
    results=[]
    freq_freq={}
    for q in queries:
        if q[0]==1:
            before=counter.get(q[1],0)
            counter[q[1]]=counter.get(q[1],0)+1
            after=counter[q[1]]
            freq_freq[before]=freq_freq.get(before, 1)-1
            freq_freq[after]=freq_freq.get(after,0)+1
        elif q[0]==2:
            before=counter.get(q[1],0)
            counter[q[1]]=max(counter.get(q[1],1)-1, 0)
            after=counter[q[1]]
            freq_freq[before]=freq_freq.get(before,1)-1
            freq_freq[after]=freq_freq.get(after,0)+1
        else:
            result=freq_freq.get(q[1],0)
            result=0 if result<=0 else 1
            results.append(result)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
