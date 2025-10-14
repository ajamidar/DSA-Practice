import sys
from collections import defaultdict, deque

def count_levels(relationships, start, end):
    # If comparing same person
    if start == end:
        return 0
        
    # Build directed graph from employee to manager
    # This represents the hierarchy properly
    graph = defaultdict(str)
    for emp, mgr in relationships:
        graph[emp] = mgr
    
    # Find path from each employee to the top of hierarchy
    def path_to_top(employee):
        path = []
        current = employee
        while current in graph:
            path.append(current)
            current = graph[current]
        path.append(current)  # Add the top manager
        return path
    
    # Get paths
    path1 = path_to_top(start)
    path2 = path_to_top(end)
    
    # Find the lowest common ancestor (LCA)
    i = len(path1) - 1
    j = len(path2) - 1
    
    # Start from the top (CEOs will match)
    while i >= 0 and j >= 0 and path1[i] == path2[j]:
        i -= 1
        j -= 1
    
    # Calculate levels between the two employees
    # This is their respective distances to LCA
    return (i + 1) + (j + 1)

# Read input
lines = []
for line in sys.stdin:
    lines.append(line.strip())

# Parse input
compare_pair = lines[0].split('/')
name1, name2 = compare_pair[0], compare_pair[1]

# Parse employee-manager relationships
relationships = []
for i in range(1, len(lines)):
    if lines[i]:  # Skip empty lines
        emp, mgr = lines[i].split('/')
        relationships.append((emp, mgr))

# Calculate and print the result
result = count_levels(relationships, name1, name2)
print(result)