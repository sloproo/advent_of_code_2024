"""
Tämä on ChatGPT:ltä pyydettyä optimoitua koodia, joka antaa valitettavasti 
väärän vastauksen. Muuten ihan hyvä."""

from heapq import heappop, heappush
from collections import defaultdict

class Tila:
    def __init__(self, paikka: tuple[int, int], suunta: str, aika: int):
        self.paikka = paikka
        self.suunta = suunta
        self.aika = aika

    def __lt__(self, other):
        return self.aika < other.aika

def read_maze(file_path):
    with open(file_path, 'r') as f:
        kartta = []
        for r in f:
            kartta.append([m for m in r.strip()])
    for y in range(len(kartta)):
        for x in range(len(kartta[y])):
            if kartta[y][x] == "E" or kartta[y][x] == "S":
                if kartta[y][x] == "E":
                    maali = (x, y)
                    kartta[y][x] = "."
                elif kartta[y][x] == "S":
                    alku = (x, y)
                    kartta[y][x] = "."
    return (kartta, alku, maali)

def bfs(kartta, alku, maali):
    directions = ['N', 'E', 'S', 'W']
    moves = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    turns = {'L': -1, 'R': 1}
    start_state = Tila(alku, 'N', 0)
    queue = []
    heappush(queue, start_state)
    visited = defaultdict(lambda: float('inf'))
    visited[(alku, 'N')] = 0
    fastest_time = float('inf')
    fastest_routes = set()

    while queue:
        tila = heappop(queue)
        x, y = tila.paikka

        if tila.paikka == maali:
            if tila.aika < fastest_time:
                fastest_time = tila.aika
                fastest_routes = {tila.paikka}
            elif tila.aika == fastest_time:
                fastest_routes.add(tila.paikka)
            continue

        # Move forward
        dx, dy = moves[tila.suunta]
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(kartta[0]) and 0 <= ny < len(kartta) and kartta[ny][nx] == ".":
            new_state = Tila((nx, ny), tila.suunta, tila.aika + 1)
            if new_state.aika < visited[(new_state.paikka, new_state.suunta)]:
                visited[(new_state.paikka, new_state.suunta)] = new_state.aika
                heappush(queue, new_state)

        # Turn left or right
        for turn, delta in turns.items():
            new_direction = directions[(directions.index(tila.suunta) + delta) % 4]
            new_state = Tila(tila.paikka, new_direction, tila.aika + 1000)
            if new_state.aika < visited[(new_state.paikka, new_state.suunta)]:
                visited[(new_state.paikka, new_state.suunta)] = new_state.aika
                heappush(queue, new_state)

    return fastest_time, fastest_routes

# Example usage
kartta, alku, maali = read_maze("input.txt")
fastest_time, fastest_routes = bfs(kartta, alku, maali)
print(f"Fastest time to reach the goal: {fastest_time}")
print(f"Number of points on any fastest route: {len(fastest_routes)}")
