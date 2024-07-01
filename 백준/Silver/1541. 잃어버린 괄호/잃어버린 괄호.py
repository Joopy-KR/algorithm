# 한개의 괄호가 아니라
# 그냥 더하기마다 괄호만 치면 되는 짱쉬운 문제였다;;;
import sys
input = sys.stdin.readline

shik = input().rstrip()
numbers = []
temp = ''
for s in shik:
    if s == '-':
        numbers.append(temp)
        numbers.append('-')
        temp = ''
    elif s == '+':
        numbers.append(temp)
        numbers.append('+')
        temp = ''
    else:
        temp += s
numbers.append(temp)

temp_symbol = ''
idx = 0

while idx < len(numbers):
    # 연산 기호면
    if not numbers[idx].isnumeric():
        if numbers[idx] == '+':
            numbers[idx] = str(int(numbers[idx - 1]) + int(numbers[idx + 1]))
            numbers.pop(idx - 1)
            numbers.pop(idx)
            idx -= 1
        else:
            idx += 1
    else:
        idx += 1

answer = 0
temp_symbol = ''
for number in numbers:
    if not number.isnumeric():
        temp_symbol = number
    else:
        if temp_symbol == '' or temp_symbol == '+':
            answer += int(number)
        else:
            answer -= int(number)
        temp_symbol = ''

print(answer)
