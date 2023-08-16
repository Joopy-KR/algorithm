"""
1. 스택을 만들어서, 연산자가 아니면 하나씩 넘어가다가
2. 연산자가 나오면, 앞에꺼, 그 앞에꺼 꺼내서 연산
"""
N = int(input())
susik = list(map(str, input()))
susik_dict = {}

for i in range(N):
    susik_dict[chr(65+i)] = input()

for j in range(len(susik)):
    if susik[j].isalpha():
        susik[j] = susik_dict[susik[j]]

stack = [0] * 101
top = -1

for k in susik:
    if k not in '+-*/':
        top += 1
        stack[top] = k
    else:
        op2 = float(stack[top])
        top -= 1
        op1 = float(stack[top])
        top -= 1
        if k == '+':
            top += 1
            stack[top] = op1 + op2
        elif k =='-':
            top += 1
            stack[top] = op1 - op2
        elif k =='*':
            top += 1
            stack[top] = op1 * op2
        elif k =='/':
            top += 1
            stack[top] = op1 / op2

print(f'{stack[0]:.2f}')