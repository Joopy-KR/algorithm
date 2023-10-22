"""
x축은 어차피 증가한다... 문제는 Y축
즉, 갑자기 y축이 올라가도 새로운 건물이고, 내려가도 새로운 건물이다
다만 생각해야 할 것은 원래 있던 건물과 이어지는가?

각 층별로 점을 찍어서 세볼까?
아 Y축이 분리가 되면 끝난거다!!!!
그니까 한번 그 이하로 내려갔다 오면 끝난거니까
싹다 세주자!!!
try except로 해줄까?
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
stack = []
building = 0
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    # 다음 층이 0층이 아니라면 (0층에는 건물이 안들어옴)
    if y != 0:
        # 이전 층이 있다면 (올라왔는지, 내려왔는지 검사하기)
        if stack:
            # 이전 층에서 올라간 거라면 (새로운 건물)
            if stack[-1] < y:
                stack.append(y)
            # 내려간 거라면, 2, 4, 6 다음에 1이 나온다면 앞의 건물들을 모두 끝내야함
            # 즉, 자기보다 같거나 큰 건물들을 모두 없애버려야 함
            else:
                while True:
                    if stack:
                        if stack[-1] > y:
                            building += 1
                            stack.pop()
                        else:
                            break
                    else:
                        break
                if stack:
                    if stack[-1] != y:
                        stack.append(y)
                else:
                    stack.append(y)
        # 이전 층이 없다면? (내가 맨 첫 건물이라면)!
        # 그냥 스택에 넣어주기
        else:
            stack.append(y)

    # 다음 층이 0층이라면 (무조건 내려온거! 건물 개수 카운트 하고 넘어가기)
    else:
        building += len(stack)
        stack = []

# 다 끝나고도 한번 검사해주기
if stack:
    building += len(stack)


print(building)