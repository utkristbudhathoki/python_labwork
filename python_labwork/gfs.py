GFS.py                                                                                                                                         # Greedy Best-First Search Algorithm

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 1,
    'H': 0
}

start = 'A'
goal = 'H'


def greedy_best_first_search(start, goal):
    open_list = [start]
    visited = []

    while open_list:
        current = min(open_list, key=lambda node: heuristic[node])
        open_list.remove(current)

        print("Visited:", current)

        if current == goal:
            print("Goal node reached!")
            return

        visited.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in open_list:
                open_list.append(neighbor)

    print("Goal node not found.")


greedy_best_first_search(start, goal)
