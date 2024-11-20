import sys

INF = sys.maxsize

def get_dir(prev_node, curr_node):
    prev_x, prev_y = prev_node
    curr_x, curr_y = curr_node

    if prev_x < curr_x:
        return "apačia"
    elif prev_x > curr_x:
        return "viršus"
    elif prev_y < curr_y:
        return "dešinė"
    elif prev_y > curr_y:
        return "kairė"


def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    distances = [[INF] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    previous_nodes = [[None] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

   
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        min_distance = INF
        current_node = None
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and distances[i][j] < min_distance:
                    min_distance = distances[i][j]
                    current_node = (i, j)

        
        if current_node is None:
            break

        current_row, current_col = current_node
        visited[current_row][current_col] = True

        
        if current_node == end:
            break

        
        for dr, dc in directions:
            neighbor_row, neighbor_col = current_row + dr, current_col + dc
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                if not visited[neighbor_row][neighbor_col]:
                    weight = grid[neighbor_row][neighbor_col]
                    if weight != INF:
                        distance = distances[current_row][current_col] + weight
                        if distance < distances[neighbor_row][neighbor_col]:
                            distances[neighbor_row][neighbor_col] = distance
                            previous_nodes[neighbor_row][neighbor_col] = (current_row, current_col)

    
    path = []
    node = end
    while node is not None:
        path.append((node[0], node[1]))
        node = previous_nodes[node[0]][node[1]]
    path.reverse()

    dirs = []
    prev_node = path[0]
    for node in path[1:]:
        dirs.append(get_dir(prev_node, node))
        prev_node = node

    return dirs


matrix = [
    [1, 1, 1, 1, 1],
    [1, INF, 1, INF, 1],
    [INF, 1, 1, 1, 1],
    [1, 1, INF, INF, INF],
    [INF, 1, 1, 1, 1]
]

start = (0, 2)  
end = (4, 3)    

dirs = dijkstra(matrix, start, end)
print("Judėjimo kryptys:", dirs)
input()
