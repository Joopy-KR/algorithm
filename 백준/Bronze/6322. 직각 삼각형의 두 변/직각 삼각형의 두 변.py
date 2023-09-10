import math

tc = 0
while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    else:
        tc += 1
        if C == -1:
            result = math.sqrt((A ** 2) + (B ** 2))
            print(f'Triangle #{tc}\nc = {result:.3f}\n')
        else:
            if C <= A or C <= B:
                print(f'Triangle #{tc}\nImpossible.\n')
            else:
                if A == -1:
                    result = math.sqrt((C ** 2) - (B ** 2))
                    print(f'Triangle #{tc}\na = {result:.3f}\n')
                elif B == -1:
                    result = math.sqrt((C ** 2) - (A ** 2))
                    print(f'Triangle #{tc}\nb = {result:.3f}\n')
