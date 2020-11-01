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


def gradingStudents(grades):
    for grade in range(0, len(grades)):
        next_mult_5 = grades[grade]

        while(next_mult_5 % 5 != 0):
            next_mult_5 += 1

        if next_mult_5 - grades[grade] < 3 and grades[grade] >= 38:
            grades[grade] = next_mult_5

    return grades


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apl = 0
    orng = 0
    for apple in apples:
        if a + apple >= s and a + apple <= t:
            apl += 1
    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            orng += 1
    print(apl)
    print(orng)


def pyListCmd(arr): #run list commands from userInput
    for x in range(0, len(arr)):
        spl = input().split(' ')
        cmd = spl[0]
        args = ','.join(spl[1:])

        if cmd != 'print':
            eval(f'arr.{cmd}({args})')
        else:
            print(arr)

def sockMerchant(n, ar):
    number = 0
    tested_colors = []
    for color in range(n):
        if ar[color] not in tested_colors:
            how_many_socks = ar.count(ar[color])
            how_many_pairs = int(how_many_socks / 2)
            number += how_many_pairs
            tested_colors.append(ar[color])
    return print(number)

def countingValleys(steps, path):
    valleyCount = 0
    sea_level = 0

    for pos in path:
        prev = sea_level
        if pos == 'U':
            sea_level += 1
        if pos == 'D':
            sea_level -= 1

        if sea_level > -1 and prev < 0:
            valleyCount += 1

    return print(valleyCount)


def jumpingOnClouds(c):
    position = 0
    steps = 0

    while(position < len(c)-2):
        if c[position+1] == 1:
            steps += 1
            position += 2
        elif c[position+1] == 0  and c[position+2] == 0:
            steps += 1
            position += 2
        else:
            steps += 1
            position += 1

    if len(c) - position == 2:
        steps += 1

    return steps


def repeatedString(s, n):
    whole = s.count('a') * (n // len(s))
    remainder =  s[:n % len(s)].count('a')

    return whole + remainder

if __name__ == '__main__':
    print(repeatedString('babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb', 860622337747))