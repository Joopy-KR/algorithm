"""
ACAYKP
CAPCAK

이 두개를 비교한다고 했을때
1. A를 돌면서 같은게 있는지 확인한후 있으면,
2. C로 넘어가고 A다음에 뭐가 같은게 있는지 확인하고
3. 이 작업을 반복하면서 길이를 세고 저장해둔다

2. 다음으로 C를 돌면서 같은게 있는지 확인한후 있으면
3. A로 넘어가고... 이렇게 반복한다.
4. 이렇게 max_len을 갱신시켜 출력한다.
"""
import sys
input = sys.stdin.readline

arr1 = list(map(str, input().rstrip()))
arr2 = list(map(str, input().rstrip()))
ln1 = len(arr1)
ln2 = len(arr2)
cnt_list = [0] * ln2

for i in range(ln1):
    max_len = 0
    for j in range(ln2):
        if max_len < cnt_list[j]:
            max_len = cnt_list[j]
        elif arr1[i] == arr2[j]:
            cnt_list[j] = max_len + 1

print(max(cnt_list))