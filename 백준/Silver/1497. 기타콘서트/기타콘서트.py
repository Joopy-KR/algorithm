from itertools import combinations

N, M = map(int, input().rstrip().split())
target = 0
result = 0
bi_musics = list()
for _ in range(N):
    name, music = input().rstrip().split()
    bi_music = 0
    for m in range(M):
        if music[m] == "Y":
            bi_music |= (1 << m)
    target |= bi_music
    if bi_music:
        bi_musics.append(bi_music)

for i in range(1, N + 1):
    for j in list(combinations(bi_musics, i)):
        temp_ans = 0
        for k in j:
            temp_ans |= k
        if temp_ans == target:
            result = len(j)
            break
    if result: break

print(result if result else -1)