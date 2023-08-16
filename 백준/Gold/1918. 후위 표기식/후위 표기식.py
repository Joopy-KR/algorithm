stack = [0] * 101
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
fx = input()
susik = ''

for x in fx:
    # 1. 숫자가 나오면 수식에 집어넣고
    if x not in '(+-*/)':
        susik += x
    # 2. 괄호 닫는 연산자가 나오면, 여는 괄호 나올때까지 팝하여 수식에 넣고
    elif x == ')':
        while stack[top] != '(':
            susik += stack[top]
            top -= 1
        top -= 1    # ( 버리기
    else:
        # 3. 수식이 나오면, isp와 icp 비교하여 만약 토큰 우선순위가 높다면 집어넣고
        if top == -1 or isp[stack[top]] < icp[x]:
            top += 1
            stack[top] = x
        # 4. top에 있는 연산자의 우선순위가 높거나 같다면, 낮은거 나올 때까지 pop하여 수식
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = x
if stack:
    while top > -1:
        susik += stack[top]
        top -= 1

print(susik)