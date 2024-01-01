N = int(input())
arr = [1] * (N + 1)
for i in range(2, N + 1): arr[i] = (arr[i - 1] + arr[i - 2] + 1) % 1000000007
print(arr[N])