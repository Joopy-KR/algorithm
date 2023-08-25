r1 = int(input())
r2 = int(input())
r3 = int(input())

if r1 == 60 and r2 == 60 and r3 == 60:
    print('Equilateral')
elif r1 + r2 + r3 == 180:
    if r1 == r2 or r2 == r3 or r1 == r3:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')