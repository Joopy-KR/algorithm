"""
제일 길게 일치하는 문자열부터 차례로 없애버리면 안되나?

하나씩 올리면서 있는지 확인하고
있다면 @ 으로 없애버린다
그리고 다시 find
"""
import sys
input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()

result = 0
idx = 0
temp = ''
while idx < len(P):
    temp += P[idx]
    # 찾는 문자열이 S에 있으면
    if S.find(temp) != -1:
        idx += 1
    # 없으면
    else:
        result += 1
        temp = ''

# 끝나고 한번 더해주기
if temp:
    result += 1

print(result)