"""
1. 거꾸로 뒤집어놓고 봐도 그리디 알고리즘
2. 5를 최대한 넣어보고, 3으로 안나눠지면 5를 하나씩 빼보자
"""
N = int(input())

max_five = N // 5

# 1. 5를 최대한 넣어보고, 3으로 안나눠지면 5를 하나씩 빼보자
while max_five != 0:
    if (N - (max_five * 5)) % 3 != 0:
        max_five -= 1
    else:
        print(max_five + ((N - (max_five * 5)) // 3))
        break
if max_five == 0:
    if N % 3 != 0:
        print(-1)
    else:
        print(N // 3)