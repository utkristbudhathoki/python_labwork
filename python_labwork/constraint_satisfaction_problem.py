# Constraint Satisfaction Problem (CSP)
# Map Coloring using Backtracking and Forward Checking

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']


def is_safe(node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def forward_check(node, color, assignment):
    for neighbor in graph[node]:
        if neighbor not in assignment:
            available = False
            for c in colors:
                if is_safe(neighbor, c, assignment):
                    available = True
                    break
            if not available:
                return False
    return True


def backtrack(assignment):
    if len(assignment) == len(graph):
        return assignment

    unassigned = [node for node in graph if node not in assignment]
    node = unassigned[0]

    for color in colors:
        if is_safe(node, color, assignment):
            assignment[node] = color

            if forward_check(node, color, assignment):
                result = backtrack(assignment)
                if result:
                    return result

            del assignment[node]

    return None


solution = backtrack({})

if solution:
    print("Valid Color Assignment:")
    for region, color in solution.items():
        print(region, "->", color)
else:
    print("No solution found.")