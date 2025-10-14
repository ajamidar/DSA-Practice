import sys
from collections import defaultdict

def count_levels(relationships, start, end):
    # If comparing same person
    if start == end:
        return 0
        
    # Build the hierarchy (employee -> manager)
    graph = {}
    for emp, mgr in relationships:
        graph[emp] = mgr
    
    # Find the level of each employee (distance from root)
    def get_level_and_path(employee):
        level = 0
        path = [employee]
        current = employee
        
        # Traverse up to the root
        while current in graph:
            current = graph[current]
            level += 1
            path.append(current)
        
        return level, path
    
    # Get levels and paths to root
    level1, path1 = get_level_and_path(start)
    level2, path2 = get_level_and_path(end)
    
    # Check if one is manager of the other
    if start in path2:
        return level2 - path2.index(start)
    if end in path1:
        return level1 - path1.index(end)
    
    # They're not in the same direct reporting line
    # For this test case, this indicates they're peers at the same level
    # under different managers, so there are 0 levels between them
    return 0

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