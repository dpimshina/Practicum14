n = int(input())

objects = {}

for line in range(n):
    lines = input().split()
    shape = lines[0]
    object = lines[1:]
    if shape not in objects:
        objects[shape] = object

word = input()

result = ""

for key, value in objects.items():
    if word in value:
        result = key

print(result)