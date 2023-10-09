"""
양쪽 옆이 짝수고 자신이 홀수라면 뽑혀야한다
1. 처음부터 가면서
2. 홀수가 나오면 홀수 카운터만큼 세주고
3. 짝수가 나오면 temp_result += 1 해주고
4. 넘어가기 전 max_result 갱신하기

시간 해결하는법 = 이전 숫자의 결과를 저장해놓고,
이전 숫자가 짝수라면 짝수 결과에서 하나 빼고 시작하고,
이전 결과가 홀수라면 이전 결과 그대로 홀수 카운트 -1 하고
이전 친구가 제일 멀리 간 곳부터 시작하자
end로 가면서  start = end 하면 된다..!
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

start = 0
end = -1
max_result = 0
temp_result = 0
odd_cnt = 0

while True:
    if end != -1:
        # 이전 숫자가 짝수라면 짝수 결과에서 하나 빼고 시작하고,
        if arr[start] % 2 == 0:
            temp_result -= 1
        # 이전 결과가 홀수라면 이전 결과 그대로 홀수 카운트 -1 하고
        else:
            odd_cnt -= 1
        start += 1

    while end < N - 1:
        end += 1
        # 3. 짝수가 나오면 temp_result += 1 해주고
        if arr[end] % 2 == 0:
            temp_result += 1
        # 2. 홀수가 나오면 홀수 카운터만큼 세주고
        else:
            odd_cnt += 1
            # 4. 넘어가기 전 max_result 갱신하기
            if odd_cnt == K + 1:
                max_result = max(max_result, temp_result)
                end -= 1
                odd_cnt -= 1
                break

    if end == N - 1:
        max_result = max(max_result, temp_result)
        break


print(max_result)
