n = int(input())

family_tree = {}

for _ in range(n):
    parent, child = input().split()

    if parent not in family_tree:
        family_tree[parent] = []

    family_tree[parent].append(child)

name = input()

def descendant(name: str) -> int:
    if name not in family_tree:
        return 0

    count = 0

    for child in family_tree[name]:
        count += 1
        count += descendant(child)

    return count

print(descendant(name))

