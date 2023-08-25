r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r3, c3 = map(int, input().split())

r4 = 0
if r1 == r2:
    r4 = r3
elif r2 == r3:
    r4 = r1
elif r1 == r3:
    r4 = r2

c4 = 0
if c1 == c2:
    c4 = c3
elif c2 == c3:
    c4 = c1
elif c1 == c3:
    c4 = c2

print(r4, c4)

