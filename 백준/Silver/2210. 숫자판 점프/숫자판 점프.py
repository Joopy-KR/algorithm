arr = [list(map(str, input().split())) for _ in range(5)]

d_r = [-1, 0, 1, 0]
d_c = [0, 1, 0, -1]
result = []

for r in range(5):
    for c in range(5):
        temp = [arr[r][c]]
        for i in range(4):
            ir = r + d_r[i]
            ic = c + d_c[i]
            if 0 <= ir < 5 and 0 <= ic < 5:
                temp.append(arr[ir][ic])
                for j in range(4):
                    jr = ir + d_r[j]
                    jc = ic + d_c[j]
                    if 0 <= jr < 5 and 0 <= jc < 5:
                        temp.append(arr[jr][jc])
                        for k in range(4):
                            kr = jr + d_r[k]
                            kc = jc + d_c[k]
                            if 0 <= kr < 5 and 0 <= kc < 5:
                                temp.append(arr[kr][kc])
                                for m in range(4):
                                    mr = kr + d_r[m]
                                    mc = kc + d_c[m]
                                    if 0 <= mr < 5 and 0 <= mc < 5:
                                        temp.append(arr[mr][mc])
                                        for n in range(4):
                                            nr = mr + d_r[n]
                                            nc = mc + d_c[n]
                                            if 0 <= nr < 5 and 0 <= nc < 5:
                                                temp.append(arr[nr][nc])
                                                temp_result = ''.join(temp)

                                                result.append(temp_result)
                                                temp.pop()
                                        temp.pop()
                                temp.pop()
                        temp.pop()
                temp.pop()
# print(result)
ans = set((tuple(result)))
# print(ans)
print(len(ans))