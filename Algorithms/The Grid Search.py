#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):

    for r in range(len(G)):
        starting_row=r
        found=True
        offset_in_row=None
        while G[r].find(P[0])>-1:
            starting_row=r
            found=True
            for r2 in range(len(P)):
                if starting_row>=len(G):
                    return "NO"
                if r2==0:
                    offset_in_row=G[starting_row].find(P[r2])
                else:
                    new_offset=G[starting_row][offset_in_row:].find(P[r2])
                    if new_offset!=0:
                        found=False
                        break
                if offset_in_row>-1:
                    if r2==0:
                        new_str="a"+P[0][1:]
                        G[r]=G[r].replace(P[0],new_str, 1)
                    starting_row+=1
                else:
                    found=False
                    break
            if found:
                return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
