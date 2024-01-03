import sys
input = sys.stdin.readline

N = int(input().rstrip())

x_lst = []
y_lst = []

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    x_lst.append(x)
    y_lst.append(y)


result = 0
for a in range(N - 2):
    for b in range(a, N - 1):
        for c in range(b, N):
            # 삼각형의 조건1 일치하는 점이 없다
            if (x_lst[a] == x_lst[b] and y_lst[a] == y_lst[b]) or (x_lst[a] == x_lst[c] and y_lst[a] == y_lst[c]) or (x_lst[b] == x_lst[c] and y_lst[b] == y_lst[c]):
                continue

            length1 = (((x_lst[a] - x_lst[b]) ** 2) + ((y_lst[a] - y_lst[b]) ** 2))
            length2 = (((x_lst[a] - x_lst[c]) ** 2) + ((y_lst[a] - y_lst[c]) ** 2))
            length3 = (((x_lst[b] - x_lst[c]) ** 2) + ((y_lst[b] - y_lst[c]) ** 2))

            if length1 > length2 and length1 > length3:
                if length2 + length3 == length1:
                    result += 1

            elif length2 > length1 and length2 > length3:
                if length1 + length3 == length2:
                    result += 1

            else:
                if length1 + length2 == length3:
                    result += 1


print(result)


