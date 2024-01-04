N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for i in range(len(arr)):
    temp = arr[i]
    arr[i] += result
    result += temp

print(sum(arr))