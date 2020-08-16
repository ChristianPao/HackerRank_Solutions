#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime  
from datetime import timedelta 

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    x=None
    if year<=1917:
        if year%100==0:
            x=datetime(year, 1, 1)+timedelta(days=254)#I cheated ^^
        else:
            x=datetime(year, 1, 1)+timedelta(days=255)
    elif year==1918:
        x=datetime(year, 1, 1)+timedelta(days=255+13)
    else:
        x=datetime(year, 1, 1)+timedelta(days=255)
    return x.strftime("%d.%m.%Y")
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
