N = input()
arr = list(map(int, input().split()))

result = 0
for i in arr:
    temp = str(i)
    for j in temp:
        if j == N:
            result += 1

print(result)
