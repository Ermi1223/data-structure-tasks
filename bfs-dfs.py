class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        self.adjacency_list[source].append(destination)

        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = []
        self.adjacency_list[destination].append(source)

    def display_graph(self):
        for city in self.adjacency_list:
            print(f"{city} -> {', '.join(self.adjacency_list[city])}")

    def bfs(self, start, goal):
        visited = set()
        queue = [(start, [start])]  # Queue of (current city, path taken)

        while queue:
            current_city, path = queue.pop(0)
            if current_city == goal:
                print("BFS path:", " -> ".join(path))
                return path

            if current_city not in visited:
                visited.add(current_city)

                for neighbor in self.adjacency_list.get(current_city, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        print(f"No path found from {start} to {goal} using BFS.")
        return None

    def dfs_recursive(self, current_city, goal, visited, path):
        visited.add(current_city)
        path.append(current_city)

        if current_city == goal:
            print("DFS path:", " -> ".join(path))
            return path

        for neighbor in self.adjacency_list.get(current_city, []):
            if neighbor not in visited:
                result = self.dfs_recursive(neighbor, goal, visited, path)
                if result:  # Path found
                    return result

        # Backtrack if no path is found from this node
        path.pop()
        return None

    def dfs(self, start, goal):
        visited = set()
        path = []
        result = self.dfs_recursive(start, goal, visited, path)

        if not result:
            print(f"No path found from {start} to {goal} using DFS.")
        return result

# Initialize the graph
city_graph = Graph()

# List of routes as given in the example
routes = [
    ("New York", "Los Angeles"),
    ("New York", "Chicago"),
    ("New York", "Houston"),
    ("Los Angeles", "Chicago"),
    ("Los Angeles", "Houston"),
    ("Chicago", "Houston"),
    ("San Francisco", "Los Angeles"),
    ("San Francisco", "Chicago"),
    ("San Francisco", "Houston"),
    ("Seattle", "Los Angeles"),
    ("Seattle", "Chicago"),
    ("Seattle", "Houston"),
    ("Boston", "Los Angeles"),
    ("Boston", "Chicago"),
    ("Boston", "Houston"),
    ("Miami", "Los Angeles"),
    ("Miami", "Chicago"),
    ("Miami", "Houston")
]

# Add each route to the graph
for source, destination in routes:
    city_graph.add_edge(source, destination)

# Example usage:
city_graph.display_graph()
print("\nFinding paths between cities:")

# BFS Example
city_graph.bfs("New York", "Seattle")

# DFS Example
city_graph.dfs("New York", "Seattle")
