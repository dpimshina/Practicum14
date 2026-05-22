n = int(input())

vocabulary = {}

for line in range(n):
    lines = input()
    rus_word, eng_word = lines.split()
    if rus_word not in vocabulary:
        vocabulary[rus_word] = eng_word

phrase = input()
words = phrase.split()
result = []

for word in words:
    if word in vocabulary:
        result.append(vocabulary[word])
    else:
        result.append(word)

print(" ".join(result))