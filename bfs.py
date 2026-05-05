from collections import deque

def bfs(graph, start):
    visited = []          # ← 4 spaces (or 1 tab)
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited