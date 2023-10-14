class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    def is_path_exists(self, start, end):
        visited = set()

        def dfs(node):
            visited.add(node)
            if node == end:
                return True
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(start)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

# Zde měňte hodnotu podle toho, které cesty chcete vyzkoušet
    start_node = 0
    end_node = 5

    if g.is_path_exists(start_node, end_node):
        print(f"Cesta existuje mezi uzly {start_node} a {end_node}.")
    else:
        print(f"Cesta neexistuje mezi uzly {start_node} a {end_node}.")