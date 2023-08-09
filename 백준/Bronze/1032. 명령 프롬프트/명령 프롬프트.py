"""
1. 하나 놓고 하나 돌면서
2. 다른 하나 놓고 하나 돌면서
같으면 pass 다르면 ?
"""


N = int(input())  # 파일 이름 개수
arr = []
for _ in range(N):
    arr.append(list(input()))


ln = len(arr[0])
is_result = False
result = ''

for c in range(ln):
    temp_word = ''
    for r in range(N):
        temp_word += arr[r][c]
    for i in range(N):
        if temp_word[0] == temp_word[0+i]:
            is_result = True
        else:
            is_result = False
            break

    if is_result:
        result += temp_word[0]
    else:
        result += '?'

print(result)