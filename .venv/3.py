n = int(input())

antonyms = {}

for line in range(n):
    lines = input()
    first_word, second_word = lines.split()
    if first_word not in antonyms:
        antonyms[first_word] = second_word

word = input()

result = ""

if word in antonyms:
    result = antonyms[word]
else:
    result = word

print(result)