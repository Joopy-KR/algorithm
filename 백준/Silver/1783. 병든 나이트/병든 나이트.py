import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
result = 0
if N == 1:
    result = 1
elif 1 < N < 3:
    if M == 1:
        result = 1
    elif M == 2:
        result = 1
    elif M == 3:
        result = 2
    elif M == 4:
        result = 2
    elif M == 5:
        result = 3
    elif M == 6:
        result = 3
    else:
        result = 4

else:
    if M == 1:
        result = 1
    elif M == 2:
        result = 2
    elif M == 3:
        result = 3
    elif M == 4:
        result = 4
    elif M == 5:
        result = 4
    else:
        result = M - 2

print(result)