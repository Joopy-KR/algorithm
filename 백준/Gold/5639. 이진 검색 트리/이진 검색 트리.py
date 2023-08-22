import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def find(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if arr[i] > arr[start]:
            mid = i
            break
    find(start + 1, mid - 1)    # 왼쪽 트리
    find(mid, end)      # 오른쪽 트리
    print(arr[start])


arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

find(0, len(arr) - 1)