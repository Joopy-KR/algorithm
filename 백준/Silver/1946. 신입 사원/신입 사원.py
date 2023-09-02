import sys
input = sys.stdin.readline

T = int(input().rstrip())
for tc in range(1, T + 1):
    N = int(input().rstrip())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().rstrip().split())))

    result = []
    arr.sort()
    interview_king = 100001
    for i in range(N):
        if arr[i][1] <= interview_king:
            interview_king = arr[i][1]
            result.append(arr[i])

    print(len(result))