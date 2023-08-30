is_valid1 = True
is_valid2 = False
dr = [2, 1, -1, -2, -2, -1, 1, 2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

result = []
cnt = 0
for i in range(36):
    order = list(map(str, input()))
    if order in result:
        is_valid1 = False
    result.append(order)
    if i >= 1:
        for j in range(8):
            nr = int(order[1]) + int(dr[j])
            nc = ord(order[0]) + int(dc[j])
            if 0 < nr < 7 and 65 <= nc < 71:
                if int(result[-2][1]) == nr and ord(result[-2][0]) == nc:
                    cnt += 1

if is_valid1:
    if cnt == 35:
        for k in range(8):
            nr = int(result[-1][1]) + int(dr[k])
            nc = ord(result[-1][0]) + int(dc[k])
            if 0 < nr < 7 and 65 <= nc < 71:
                if int(result[0][1]) == nr and ord(result[0][0]) == nc:
                    print("Valid")
                    break
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")