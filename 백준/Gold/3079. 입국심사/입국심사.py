import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

arr = [int(input().rstrip()) for _ in range(N)]

# 이분탐색 범위 설정 0 ~ 최대시간 * 전체인원
start = 0
end = max(arr) * M

# 젤 큰값
result = max(arr) * M

while start <= end:
    mid = (start + end) // 2

    # 시간을 기준으로 이분탐색 하는 것
    # 시간을 반씩 잘라가면서 모든 사람들을 검색할 수 있는 최소 시간을 찾아본다
    temp = 0
    for i in range(N):
        # 한 검색대 당 mid 시간에 검색할 수 있는 사람 수를 더해준다
        temp += mid // arr[i]

    # 다 더했는데 전체 인원보다 같거나 많다면?
    if temp >= M:
        # 절반 이하로
        end = mid - 1
        result = min(result, mid)

    # 아니면?
    else:
        start = mid + 1

print(result)