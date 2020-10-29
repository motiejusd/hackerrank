import math
import os
import random
import re
import sys


def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for x in range(0, len(arr)):
        if arr[x] > 0:
            pos += 1
        if arr[x] < 0:
            neg += 1
        if arr[x] == 0:
            zer += 1
    return ['{:.6f}'.format(pos/len(arr)), '{:.6f}'.format(neg/len(arr)), '{:.6f}'.format(zer/len(arr))]

if __name__ == '__main__':
    print(plusMinus(arr))