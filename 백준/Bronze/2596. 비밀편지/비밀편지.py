import sys
input = sys.stdin.readline

solution = {'000000': 'A', '001111': 'B', '010011': 'C', '011100': 'D', '100110': 'E', '101001': 'F', '110101': 'G', '111010': 'H'}

N = int(input().rstrip())
lst = list(map(str, input().rstrip()))
keys = list(solution.keys())
values = list(solution.values())
result = []
is_true = True
idx = 0

for s in range(0, len(lst), 6):
    idx += 1
    temp = lst[s: s + 6]
    if temp in keys:
        for n in range(8):
            if temp == keys[n]:
                result += values[n]
    else:
        cnt2 = 0
        for j in range(8):
            cnt = 0
            for k in range(6):
                if temp[k] != keys[j][k]:
                    cnt += 1
            if cnt <= 1:
                result.append(values[j])
                break
            else:
                cnt2 += 1
        if cnt2 == 8:
            is_true = False
            break

if is_true:
    print(''.join(result))
else:
    print(idx)