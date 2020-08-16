#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    c_a=Counter()
    c_b=Counter()
    for char in a:
        c_a[char]+=1
    for char in b:
        c_b[char]+=1
    to_remove=0
    for val in (c_a-c_b).values():
        to_remove+=val
    for val in (c_b-c_a).values():
        to_remove+=val   
    return to_remove

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
