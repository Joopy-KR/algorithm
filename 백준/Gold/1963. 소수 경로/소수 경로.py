import sys
input = sys.stdin.readline
from collections import deque

def isPrime():
    numbers = [0] * 10000
    for i in range(2, 100):
        to_test_range = 10000 // i
        if numbers[i] == 0:
            for j in range(i, to_test_range + 1):
                test_num = i * j
                if test_num < 10000 and numbers[test_num] == 0:
                    numbers[test_num] = 1
    return numbers

result = isPrime()

def change_password(start):
    visited = [0] * 10000
    visited[start] = 1
    queue = deque([(start, 0)])
    while queue:
        tn, tc = queue.popleft()
        if tn == num2:
            return tc

        str_tn = str(tn)
        for i in range(4):
            copy_tn = list(str_tn)
            for j in range(10):
                copy_tn[i] = str(j)
                new_str_tn = ''.join(copy_tn)
                nn = int(new_str_tn)
                if nn >= 1000 and result[nn] == 0 and visited[nn] == 0:
                    queue.append((nn, tc + 1))
                visited[nn] = 1
    return 'Impossible'

T = int(input())
for _ in range(T):
    num1, num2 = map(int, input().split())
    print(change_password(num1))
