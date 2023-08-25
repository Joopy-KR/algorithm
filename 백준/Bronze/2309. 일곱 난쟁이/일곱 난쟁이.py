total_sum = 0
arr = []
for i in range(9):
    arr.append(int(input()))
    total_sum += arr[i]

arr.sort()
is_finish = False

for j in range(8):
    if not is_finish:
        for k in range(1, 9):
            if total_sum - (arr[j] + arr[k]) == 100:
                arr[j] = 0
                arr[k] = 0
                is_finish = True
                break
    else:
        break


for m in arr:
    if m == 0:
        pass
    else:
        print(m)