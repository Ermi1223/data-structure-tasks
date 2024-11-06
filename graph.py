class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []  # List to store references to adjacent nodes

    def add_edge(self, node):
        """Adds an edge from this node to another node."""
        self.adjacent.append(node)
    
    def __str__(self):
        """Return a string representation of the node and its edges."""
        adj_values = [str(neighbor.value) for neighbor in self.adjacent]
        return f"{self.value} -> {', '.join(adj_values)}"


class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes by value

    def add_node(self, value):
        """Adds a node to the graph."""
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        else:
            print(f"Node {value} already exists.")

    def add_edge(self, from_value, to_value):
        """Adds a directed edge from one node to another."""
        if from_value not in self.nodes:
            self.add_node(from_value)
        if to_value not in self.nodes:
            self.add_node(to_value)
        
        self.nodes[from_value].add_edge(self.nodes[to_value])

    def __str__(self):
        """Return a string representation of the graph."""
        result = ""
        for node in self.nodes.values():
            result += str(node) + "\n"
        return result


# Example usage:
graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)

print(graph)
