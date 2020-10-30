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


def birthdayCakeCandles(candles):
    tallest = max(candles)
    tallest_count = candles.count(tallest)
    print(tallest_count)


# s = '12:05:45AM'
def timeConversion(s):
    hours = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]
    t = s[8:10]
    print('t:', t)
    print('hours:', hours)

    if(t == 'PM' and int(hours) < 12):
        hours = int(hours)+12

    if(t == 'AM' and int(hours) == 12):
        hours = '00'

    return f"{hours}:{minutes}:{seconds}"


def dimOfCuboid(x, y, z, n): # returns all possible coordinations for cuboid except if x+y+z == n
    result = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n]
    return result


def runnerUp(scores):
    first = max(scores)
    second = 0
    for x in scores:
        if x < first and x > second:
            second = x
    return second


#print list of names with second to lowest score from nested list
def secToLowest(li):
    scores = list()
    lowest_2nd_list = list()

    for n, s in li:
        scores.append(s)

    lowest = min(scores)
    lowest_2nd = max(scores)

    for l in scores:
        if l < lowest_2nd and lowest < l:
            lowest_2nd = l

    for name, score in li:
        if score == lowest_2nd:
            lowest_2nd_list.append(name)

    lowest_2nd_list.sort()

    for x in lowest_2nd_list:
        print(x)

if __name__ == '__main__':
    print('Hi')