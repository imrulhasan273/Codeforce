__author__ = 'Md. Imrul Hasan @UAP-CSE'
"""A. Adjacent Replacements"""

def func(n, arr):

    for i in range(0, n):
        if arr[i] % 2 == 0:
            arr[i]-=1
            
    return " ".join(str(_) for _ in arr)
    

if __name__ == "__main__":
    
    n = int(input())    
    arr = list(map(int, input().split(" ")))
    print(func(n, arr))