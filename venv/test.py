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
def staircase(n):
    for i in range(1, n + 1):
        print(str('#' * i).rjust(n))
def miniMaxSum(arr):
    mi = sum(arr)-max(arr)
    ma = sum(arr)-min(arr)
    print(mi)
    print(ma)

    return True
candles = [4,4,1,3]
def birthdayCakeCandles(candles):
    return True
if __name__ == '__main__':
    birthdayCakeCandles(candles)