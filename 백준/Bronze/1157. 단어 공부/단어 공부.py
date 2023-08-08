"""
1. cnt = [0] * 126개 만들고
2. 문자열 돌면서 ord로 바꿔주고
3. ord 번호를 인덱스로 cnt 숫자 하나 올려주고

4. 다 끝나고 cnt중에서 소문자를 대문자로 바꿔줌 (숫자 뺴주자)
5. cnt 리스트 돌면서 숫자 젤 높은 거 출력 (2개 이상이면 ? 출력)
6. 그 숫자 다시 chr 로 문자로 바꿔주고
7. 출력
"""

arr = list(input())


def doing_homework():
    # 1. cnt = [0] * 126개 만들고
    cnt = [0] * 126

    # 2. 문자열 돌면서 ord로 바꿔주고
    for s in arr:
        # 3. ord 번호를 인덱스로 cnt 숫자 하나 올려주고
        cnt[ord(s)] += 1

    # 4. 다 끝나고 cnt 중에서 소문자를 대문자로 바꿔줌 (숫자 뺴주자)
    for i in range(26):
        cnt[65+i] += cnt[97+i]

    # 4-2. 소문자 친구들을 리스트에서 보내줘야함
    for j in range(96, 126):
        cnt[j] = 0

    # 5. cnt 리스트 돌면서 숫자 젤 높은 거 출력 (2개 이상이면 ? 출력)
    max_idx = 0
    for k in cnt:
        if k > max_idx:
            max_idx = k

    bad_num = 0
    for l in cnt:
        if l == max_idx:
            bad_num += 1
            if bad_num == 2:
                return '?'

    # 6. 그 숫자 다시 chr 로 문자로 바꿔줌
    result = chr(cnt.index(max_idx))

    return result


print(doing_homework())