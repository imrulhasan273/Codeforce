__author__ = 'Md. Imrul Hasan @UAP-CSE'
"""A. Add Odd or Subtract Even"""

def func(a, b):
    
    diff = a - b

    if diff == 0:
        return diff

    elif diff > 0:
        if diff % 2 == 0:
            return 1
        else:
            return 2
    else:
        if diff % 2 == 0:
            return 2
        else:
            return 1


if __name__ == "__main__":
    
    t = int(input())
    for _ in range(0, t):
        a, b = map(int, input().split(" "))
        print(func(a, b))