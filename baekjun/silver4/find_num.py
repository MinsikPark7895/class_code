# 1920번
import sys

N = int(sys.stdin.readline())

A = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

s = ''
for num in nums:
    if num in A:
        s += (str(1)+'\n')
    else:
        s += (str(0)+'\n')

print(s)