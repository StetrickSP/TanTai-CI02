graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
}
graph2 = {
    0: [4],
    1: [2],
    2: [1],
    3: [4],
    4: [0, 3]
}

def check_connect(graph, start, end):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node == end:
            visited.add(node)
            return True
        
        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return False

print(check_connect(graph2, 4, 2)) 

        