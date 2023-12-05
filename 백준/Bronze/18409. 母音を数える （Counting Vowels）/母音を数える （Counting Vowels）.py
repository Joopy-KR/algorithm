N = int(input())
S = input()

vowel = ['a', 'e', 'i', 'o', 'u']
result = 0

for i in S:
    if i in vowel:
        result += 1

print(result)