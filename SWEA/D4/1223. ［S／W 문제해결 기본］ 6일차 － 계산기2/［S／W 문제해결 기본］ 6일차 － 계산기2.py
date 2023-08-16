"""
중위 표기식 후위 표기식으로 바꾸기
1. 숫자가 나오면 수식에 집어넣고
2. 괄호 닫는 연산자가 나오면, 여는 괄호 나올때까지 팝하여 수식에 넣고
3. 수식이 나오면, isp와 icp 비교하여 만약 토큰 우선순위가 높다면 집어넣고
4. top에 있는 연산자의 우선순위가 높거나 같다면, 낮은거 나올 때까지 pop하여 수식
"""
# 후위 표기식으로 바꾸기
for tc in range(1, 11):

    N = int(input())

    stack = [0] * (N + 1)
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

    """
    후위 표기식 계산하기
    1. 앞에서 하나씩 돌면서 숫자가 나오면 top += 1 해서 스택에 넣고
    2. 연산자가 나오면 앞에 두개 꺼내서
    3. top +=1 한다음에 그 자리에 연산 값 넣어주기
    4. 마지막에 하나 남았을 숫자 출력해주기
    """
# 후위 표기식 계산하기
    stack = [0] * (N + 1)
    top = -1

    for x in susik:
        # 1. 앞에서 하나씩 돌면서 숫자가 나오면 top += 1 해서 스택에 넣고
        if x not in '+-*/':  # 숫자라면
            top += 1
            stack[top] = int(x)
        else:  # 연산자라면
            # 2. 연산자가 나오면 앞에 두개 꺼내서
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op1 + op2
            elif x == '-':
                top += 1
                stack[top] = op1 - op2
            elif x == '*':
                top += 1
                stack[top] = op1 * op2
            elif x == '/':
                top += 1
                stack[top] = op1 / op2

    print(f'#{tc} {int(stack[top])}')