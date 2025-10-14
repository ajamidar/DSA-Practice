import sys

def is_happy(n):
    # Set to store numbers we've seen to detect cycles
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        # Calculate sum of squares of digits
        n = sum(int(digit)**2 for digit in str(n))
    
    # If we reached 1, it's happy; otherwise, we got stuck in a cycle
    return n == 1

# Process each line of input
for line in sys.stdin:
    num = int(line.strip())
    # Output 1 for happy numbers, 0 for unhappy numbers
    print(1 if is_happy(num) else 0)