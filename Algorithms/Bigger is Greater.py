#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    """
    You iterate from last char, as soon as there's a smaller character, aka the
    current substr is not the biggest with the current chars, find the smalled char
    which is bigger than left bound, append the rest in increasing order.
    """
    seen_chars=[w[-1]]
    if len(w)==1:
        return "no answer"
    found=False
    for left_i in range(len(w)-2, -1, -1):
        
        if w[left_i]<w[left_i+1]:
            found=True
            break
        seen_chars.append(w[left_i])
    if not found:
        return "no answer"
    sorted_chars="".join(seen_chars)
    # Put left_i char in order
    index_left_i_char_in_sorted=0
    while w[left_i]>=sorted_chars[index_left_i_char_in_sorted]:
        index_left_i_char_in_sorted+=1
    sorted_chars=sorted_chars[:index_left_i_char_in_sorted]+w[left_i]+sorted_chars[index_left_i_char_in_sorted:]
    
    found=False
    for i_biggest_next_char in range(index_left_i_char_in_sorted+1, len(sorted_chars)):
        if sorted_chars[i_biggest_next_char]>w[left_i]:
            found=True
            next_char=sorted_chars[i_biggest_next_char]
            break
    if not found:
        return "no answer"
    sorted_prefix=sorted_chars.replace(next_char, "", 1)
    return w[:left_i]+next_char+sorted_prefix

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
