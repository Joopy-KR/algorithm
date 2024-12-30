"""
2차원 배열 뒷 값으로 역순 정렬 후
큰것부터 내려오다가 자기보다 끝나는 시간에 관계없이 "시작시간이 더 빠르면" 기준으로 잡기
그 상태로 무사히 "시작시간"을 통과 (끝 시간이 더 빠르면)하면 기준 변경 및 +1
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
schedules = [list(map(int, input().rstrip().split())) for _ in range(N)]
schedules.sort(key=lambda x:(-x[1], -x[0]))
latest_start = -1
result = 0
for idx, schedule in enumerate(schedules):
    # 맨 처음 경우는 제외
    if idx == 0:
        latest_start = schedule[0]
        continue
    # 1. 시작시간이 다음 끝 시간보다 빠른가
    if schedule[1] <= latest_start:
        result += 1
        latest_start = schedule[0]
    # 2. 시작시간이 이전 시작 시간보다 느린가
    elif schedule[0] >= latest_start:
        latest_start = schedule[0]

print(result + 1)