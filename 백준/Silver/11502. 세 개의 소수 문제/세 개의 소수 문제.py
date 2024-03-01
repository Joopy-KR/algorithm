import math
import sys
input = sys.stdin.readline

def isPrime(N, array):
    for i in range(2, int(math.sqrt(N)) + 1):
        if array[i] == True:
            for j in range(i * 2, N + 1, i):
                array[j] = False
    return array


def solution(N, arr):
    for a in range(1, N + 1):
        if not arr[a]:
            continue
        for b in range(1, N + 1):
            if not arr[b]:
                continue
            for c in range(1, N + 1):
                if not arr[c]:
                    continue

                if a + b + c == N:
                    print(a, b, c)
                    return


T = int(input().rstrip())
arr = [True] * 1001
arr[0] = arr[1] = False
for _ in range(T):
    N = int(input().rstrip())
    arr = isPrime(N, arr)
    solution(N, arr)
