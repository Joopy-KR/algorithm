import sys
import re

T = int(input())

for _ in range(1, T + 1):
    code = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(code)

    if m:
        print('YES')
    else:
        print('NO')