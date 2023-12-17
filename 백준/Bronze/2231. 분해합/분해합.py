N = int(input())

for i in range(1000000):
    number = i
    lst = list(map(int, str(i)))
    if number + sum(lst) == N:
        print(number)
        break
    if number > N:
        print(0)
        break
else:
    print(0)