N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()

distance = []
for i in range(1, N):
    distance.append(arr[i] - arr[i - 1])

distance.sort()

for _ in range(K - 1):
    if distance:
        distance.pop()

print(sum(distance))