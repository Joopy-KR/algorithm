import string

arr = list(map(str, input()))
alpha = string.ascii_lowercase

for i in alpha:
    if i in arr:
        print(arr.index(i), end=' ')
    else:
        print(-1, end=' ')