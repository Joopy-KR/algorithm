#이러지 말고 그냥 모든 글자 ord로 바꾼다음에 다른게 한개 이하인지 확인하면 되는거 아닌가?

import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = 0
key = list(map(str, input().rstrip()))
key_ord = [0] * 128

for i in key:
    key_ord[ord(i)] += 1

for _ in range(N - 1):
    check = list(map(str, input().rstrip()))
    if len(key) == len(check):
        # 서로 길이가 같으면 한글자만 바뀌었는지 확인해야함
        result_ord = [0] * 128
        check_ord = [0] * 128
        cnt = 0
        for j in check:
            check_ord[ord(j)] += 1

        # 서로 빼주기
        for k in range(128):
            result_ord[k] = abs(key_ord[k] - check_ord[k])

        for n in result_ord:
            cnt += n

        # 한개가 바뀌고(한개차이), 한개가 달라졌으므로(한개차이) 변화는 두개
        if cnt == 2 or cnt == 0:
            result += 1

    # 길이가 다르면 뭔가가 추가되거나 빠진것임. 바뀐게 두개 미만이어야함
    else:
        result_ord = [0] * 128
        check_ord = [0] * 128
        cnt = 0
        for j in check:
            check_ord[ord(j)] += 1

        # 서로 빼주기
        for k in range(128):
            result_ord[k] = abs(key_ord[k] - check_ord[k])

        for n in result_ord:
            cnt += n

        # 무언가가 추가되거나, 삭제된 것이므로 변화는 한번
        if cnt < 2:
            result += 1

print(result)


# for i in range(N):
#     if i == 0:
#         key = list(map(str, input()))
#     else:
#         arr = list(map(str, input()))
#         if abs(len(arr) - len(key)) >= 2:
#             continue
#         else:
#             total = 0
#             cnt = 0
#             yes_cnt = 0
#             for j in arr:
#                 if j not in key:
#                     cnt += 1
#                     total += 1
#                     # 다른 글자가 두개 이상인지 검사
#                     if cnt >= 2:
#                         break
#                 else:
#                     # 한개까지는 봐줌
#                     yes_cnt += 1
#                     # "같은게" 두개가 있다면 뭔가 바뀐거임
#                     if yes_cnt == 2:
#                         total += 1
#                     # 세개가 있다면 틀린거임
#                     elif yes_cnt >= 3:
#                         break
#             else:
#                 # 바뀐게 두개 이상이라면
#                 if total >= 2:
#                     continue
#                 else:
#                     result += 1
#
# print(result)


