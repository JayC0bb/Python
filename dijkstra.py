def dijkstra(graph, start, file):
    num_nodes = len(graph)
    costList = [float('inf')] * num_nodes
    preds = [-1] * num_nodes
    visited = [False] * num_nodes
    costList[start] = 0

    for _ in range(num_nodes):
        # Najdi uzel ktery jeste nebyl navstiven a ma nejmensi hodnotu
        min_cost = float('inf')
        min_node = -1
        for node in range(num_nodes):
            if not visited[node] and costList[node] < min_cost:
                min_cost = costList[node]
                min_node = node

        if min_node == -1:
            break

        visited[min_node] = True

        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[min_node][neighbor] > 0:
                new_cost = costList[min_node] + graph[min_node][neighbor]
                if new_cost < costList[neighbor]:
                    costList[neighbor] = new_cost
                    preds[neighbor] = min_node

    with open(file, "w") as f:
        f.write("Cost List: " + str(costList) + "\n")
        f.write("Predecessors: " + str(preds) + "\n")

    print("Cost List:", costList)
    print("Predecessors:", preds)

graph = [
    [0, 4, 5, 0, 3],
    [4, 0, 2, 4, 0],
    [5, 2, 0, 0, 1],
    [0, 4, 0, 0, 2],
    [3, 0, 1, 2, 0],
]

dijkstra(graph, 0, "file.txt")