import math
import sys
input = sys.stdin.readline

def is_prime(X):
    for i in range(2, int(math.sqrt(X)) + 1):
        if X % i == 0:
            return False
    return True

N = int(input())
def solution(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if is_prime(number * 10 + i):
                solution(number * 10 + i)

solution(2)
solution(3)
solution(5)
solution(7)
