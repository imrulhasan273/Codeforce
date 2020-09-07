__author__ = 'Md. Imrul Hasan @UAP-CSE'
"""A. Alarm Clock"""

import math

def func(a, b, c, d):

    if b>=a:
        return b

    elif c<=d:
        return -1

    else:
        nSleepTime = a - b
        intervalAlerm = c - d

        alermNeeded = math.ceil(nSleepTime / intervalAlerm)
        return int(alermNeeded * c) + b


if __name__ == "__main__":

    t = int(input())

    results = list()
    for _ in range(0, t):
        a, b, c, d = map(int, input().split(" "))
        results.append(func(a, b, c, d))

    for result in results:
        print(result)