arr = list(map(str, input()))
result = [0] * 26
for i in arr:
    result[ord(i) - ord('a')] += 1

for j in result:
    print(j, end=' ')
