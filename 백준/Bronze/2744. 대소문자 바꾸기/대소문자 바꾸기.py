arr = list(map(str, input()))
for i in range(len(arr)):
    if arr[i].isupper():
        arr[i] = arr[i].lower()
    else:
        arr[i] = arr[i].upper()

print(''.join(arr))