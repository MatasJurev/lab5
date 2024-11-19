import sys
import heapq
import math

INF = sys.maxsize


def dijkstra(graph, start, end):
    num_nodes = len(graph)
    distances = [INF] * num_nodes
    previous_nodes = [-1] * num_nodes
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor in range(num_nodes):
            weight = graph[current_node][neighbor]
            if weight != INF:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    node = end
    while node != -1:
        path.append(node + 1)
        node = previous_nodes[node]
    path.reverse()

    return path


def main():
    graph = [
        # 1 2 3 4 5
        [INF, 10, INF, 30, 100], # 1
        [10, INF, 50, INF, INF], # 2
        [INF, 50, INF, 20, 10], # 3
        [30, INF, 20, INF, 60], # 4
        [100, INF, 10, 60, INF], # 5
    ]

    start_node = 0
    end_node = 4
    shortest_path = dijkstra(graph, start_node, end_node)

    print("Trumpiausias kelias tarp viršūnių 1 ir 5:", shortest_path)
    input()


if __name__ == "__main__":
    main()
