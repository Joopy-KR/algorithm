def solve(arr):
    result = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            result += cnt
            cnt += 1
        else:
            result += cnt
            cnt = 0
    result += cnt
    return result


N = int(input())

for _ in range(N):
    arr = input()
    print(solve(arr))