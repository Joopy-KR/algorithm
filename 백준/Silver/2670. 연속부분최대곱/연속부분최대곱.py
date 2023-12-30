N = int(input())
arr = []
for _ in range(N):
    arr.append(float(input()))

for i in range(1, N):
    arr[i] = max(arr[i], arr[i] * arr[i - 1])

print('%0.3f' % max(arr))