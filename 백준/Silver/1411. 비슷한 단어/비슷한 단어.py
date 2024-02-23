import math
import sys
input = sys.stdin.readline

N = int(input().rstrip())
word_len = 0
result_dict = dict()

for tc in range(N):
    word = input().rstrip()
    check = dict()
    idx = 0
    temp = []

    for w in word:
        d = check.get(ord(w) - 97, -1)
        # 아직 없으면
        if d == -1:
            idx += 1
            check[ord(w) - 97] = idx
            temp.append(idx)
        else:
            temp.append(d)

    result_dict.setdefault(tuple(temp), 0)
    result_dict[tuple(temp)] += 1

result = 0
for r in result_dict.values():
    result += math.comb(r, 2)

print(result)
