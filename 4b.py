import heapq

class Node:
    def __init__(self, name, heuristic, parent=None):
        self.name = name
        self.heuristic = heuristic
        self.parent = parent
    
    def __lt__(self, other):
        return self.heuristic < other.heuristic

def best_first_search(graph, start, goal, heuristic_values):
    open_list = []
    closed_list = set()
    
    heapq.heappush(open_list, Node(start, heuristic_values[start]))

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]
        
        if current_node.name in closed_list:
            continue
        
        closed_list.add(current_node.name)
        
        for neighbor in graph.get(current_node.name, []):
            if neighbor not in closed_list:
                heapq.heappush(open_list, Node(neighbor, heuristic_values[neighbor], current_node))

    return None

# Take custom input for the graph and heuristic values
def get_input():
    graph = {}
    heuristic_values = {}

    print("Enter the graph structure:")
    n = int(input("Enter number of nodes: "))
    
    for _ in range(n):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors for {node} (comma separated): ").split(",")
        graph[node] = [neighbor.strip() for neighbor in neighbors]
        
    print("\nEnter heuristic values:")
    for _ in range(n):
        node = input("Enter node name for heuristic: ")
        heuristic = int(input(f"Enter heuristic value for {node}: "))
        heuristic_values[node] = heuristic
    
    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")
    
    return graph, heuristic_values, start, goal

# Main execution
if __name__ == "__main__":
    graph, heuristic_values, start_node, goal_node = get_input()
    path = best_first_search(graph, start_node, goal_node, heuristic_values)
    
    if path:
        print(f"\nPath from {start_node} to {goal_node}: {path}")
    else:
        print(f"\nNo path found from {start_node} to {goal_node}.")

