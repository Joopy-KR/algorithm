"""
1. 제일 고리가 적은 체인부터 소모시키자. 다쓰면 걔를 엮을 필요는 없는거니까
2. 그러므로 생각을 해보자.
3. 결국 판단은 "다 묶였나" 를 기준으로 해야함. 이걸 어떻게 알수가 있지?
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()
start = 0
end = N - 1
result = 0

while start < end:
    arr[start] -= 1
    end -= 1
    result += 1

    if arr[start] == 0:
        start += 1

print(result)