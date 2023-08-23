"""
1. 꽉꽉마을 배열을 만들어주고
2. 숫자를 추가하되,
3. 만약 해당 칸에 1을 제외한 조상노드들이 비어있다면 무사히 가는거고
4. 만약 하나라도 차있다면, 추가하진 말고 처음 마주하는 점유된 땅 번호 출력
"""
import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
guakguak_village = [0] * (N + 1)

for i in range(1, Q + 1):
    duck = int(input().rstrip())
    living_duck = 0
    is_duck = True
    cnt = duck
    while cnt >= 2:
        if guakguak_village[cnt] != 0:
            living_duck = cnt
            is_duck = False
        cnt //= 2
    if not is_duck:
        print(living_duck)
    else:
        guakguak_village[duck] = 1
        print(0)