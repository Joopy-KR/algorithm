"""
1. 앞에서부터 쭉 읽으면서
2. 거꾸로 뒤집은 문자열을 처음부터 계속 매칭시켜본다
3. 만약 제일 많이 겹치는게 있다면, 잠깐만
4. 근데 뒤에 추가하는거기 때문에, 가장 짧게 추가하려면, 어떻게든 뒤에서터 붙여야 한다...

뒤집어놓고 오른쪽으로 이동시키면서

 aaad
 ddda
  ddda

abcd
dcba
 dcba
  dcba
   dcba

abcdba

abdcba
 abdcba
  abdcba

이렇게 이동하면서 제일 겹치는게 많다면 원래배열 + 튀어나온 배열 해서 저장시키고
전부다 조사하면 됨!
"""
import sys
input = sys.stdin.readline


# arr이 원래 배열
# check이 뒤집힌 배열
check = list(map(str, input().strip()))
arr = check[:]
check.reverse()
max_same = -1
result = []

# 처음부터 끝 문자까지를 시작으로 각각 보면서 비교
for i in range(len(arr)):
    temp_same = 0
    j = 0
    while i + j < len(check):
        if arr[i + j] == check[j]:
            temp_same += 1
        else:
            if temp_same > max_same:
                if i == 0:
                    result = arr[:]
                else:
                    result = arr[:] + check[-i:]
                for k in range(len(result) // 2):
                    if result[k] != result[-(k + 1)]:
                        break
                else:
                    max_same = temp_same
            break
        j += 1

    else:
        if temp_same >= max_same:
            max_same = temp_same
            if i == 0:
                result = arr[:]
            else:
                result = arr[:] + check[-i:]


print(len(result))
