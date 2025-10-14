import sys
from collections import defaultdict, deque

def count_levels(relationships, start, end):
    # Build adjacency list for the organization (undirected graph)
    graph = defaultdict(list)
    for emp, mgr in relationships:
        graph[emp].append(mgr)
        graph[mgr].append(emp)
    
    # BFS to find shortest path
    visited = set()
    queue = deque([(start, 0)])  # (employee, distance)
    visited.add(start)
    
    while queue:
        current, distance = queue.popleft()
        
        if current == end:
            return distance
        
        for connection in graph[current]:
            if connection not in visited:
                visited.add(connection)
                queue.append((connection, distance + 1))
    
    return -1  # Not found

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