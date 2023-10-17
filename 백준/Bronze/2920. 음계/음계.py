arr = list(map(int, input().split()))

asc_cnt = 1
dsc_cnt = 1
for i in range(len(arr) - 1):
    if arr[i] + 1 == arr[i + 1]:
        asc_cnt += 1
    elif arr[i] - 1 == arr[i + 1]:
        dsc_cnt += 1
    else:
        print("mixed")
        break
else:
    if asc_cnt == 8:
        print("ascending")
    elif dsc_cnt == 8:
        print("descending")