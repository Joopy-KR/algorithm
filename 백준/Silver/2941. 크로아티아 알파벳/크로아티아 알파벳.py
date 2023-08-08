poor_croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = list(input())
result = 0

for i in range(len(word)):
    if i + 1 < len(word):
        temp_word = word[i] + word[i + 1]

        if temp_word in poor_croatia:
            result += 1
            word[i] = 'x'
            word[i + 1] = 'x'

    if i + 2 < len(word):
        temp_word = word[i] + word[i + 1] + word[i + 2]

        if temp_word == "dz=":
            result += 1
            word[i] = 'x'
            word[i + 1] = 'x'
            word[i + 2] = 'x'

for s in word:
    if s != 'x':
        result += 1

print(result)
