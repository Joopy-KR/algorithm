import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = set(map(int, input().rstrip().split()))
M = int(input().rstrip())
check = list(map(int, input().rstrip().split()))

for i in check:
    if i in A:
        print(1)
    else:
        print(0)
