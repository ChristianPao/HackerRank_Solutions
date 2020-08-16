#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    counter=Counter()
    anagrams=0
    for window_size in range(len(s)):
        for j in range(0, len(s)-window_size):
            counter[''.join(sorted(s[j:j+window_size+1]))]+=1
    for k, e in counter.items():
        anagrams+=(e-1)*(e)/2
    return int(anagrams)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
