import sys

INF = sys.maxsize


def get_dir(prev_node, curr_node):
    #2 - viršus, 1 - dešinė, 4 - apačia, 3 - kairė

    prev_x, prev_y = prev_node
    curr_x, curr_y = curr_node

    if prev_x < curr_x:
        return 4
    elif prev_x > curr_x:
        return 2
    elif prev_y < curr_y:
        return 1
    elif prev_y > curr_y:
        return 3

def get_command(prev_dir, dir):
    ans = dir-prev_dir
    return ans if ans >= 0 else ans+4

def addm(path,dirs):
    dirs.insert(0, 4)
    dirs.insert(0, 4)
    dirs.append(4)
    path.insert(0, (-1, 2))
    path.append((5, 3))
    return path,dirs

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

    return path, dirs

def print_table(path, dirs):
    path, dirs = addm(path,dirs)
    #print(path,dirs)
    #print(len(path), len(dirs))
    #print()

    for i in range(1,len(path)):
        print(f"{path[i]} | {dirs[i-1]},{dirs[i]} | {get_command(dirs[i-1],dirs[i])}")

matrix = [
    [1, 1, 1, 1, 1],
    [1, INF, 1, INF, 1],
    [INF, 1, 1, 1, 1],
    [1, 1, INF, INF, INF],
    [INF, 1, 1, 1, 1]
]

start = (0, 2)  
end = (4, 3)    

path, dirs = dijkstra(matrix, start, end)
print_table(path, dirs)
