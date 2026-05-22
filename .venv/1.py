words = input().split()
frequency = {}

for word in words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

result = sorted(frequency, key=lambda x: x, reverse=True)

print(*result, sep="\n")
