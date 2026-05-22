n = int(input())
m = int(input())

graph = {}

for _ in range(m):
    city1, city2, distance = input().split()
    distance = int(distance)

    if city1 not in graph:
        graph[city1] = []

    if city2 not in graph:
        graph[city2] = []

    graph[city1].append((city2, distance))
    graph[city2].append((city1, distance))

start, finish = input().split()

def distance(start: str, finish: str) -> int:
    distances = {}

    for city in graph:
        distances[city] = float('inf')

    distances[start] = 0

    visited = set()

    while True:
        current_city = None
        current_distance = float('inf')

        for city in distances:
            if city not in visited and distances[city] < current_distance:
                current_distance = distances[city]
                current_city = city

        if current_city is None:
            break

        if current_city == finish:
            return distances[current_city]

        visited.add(current_city)

        for neighbor, distance in graph[current_city]:
            new_distance = distances[current_city] + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances[finish]

print(distance(start, finish))