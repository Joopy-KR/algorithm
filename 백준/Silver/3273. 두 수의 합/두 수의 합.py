N = int(input())
arr = list(map(int, input().split()))
arr.sort()
X = int(input())
result = 0

left = 0
right = N - 1

while left < right:
    if arr[left] + arr[right] > X:
        right -= 1
    elif arr[left] + arr[right] < X:
        left += 1
    else:
        result += 1
        left += 1

print(result)

