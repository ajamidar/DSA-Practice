import math
import os
import random
import re
import sys

def countSignals(frequencies, filterRanges):
    # Write your code here
    list_init, list_end, filter, result = [], [], [], []

    for list in filterRanges:
        list_init.append(list[0])
        list_end.append(list[1])
    filter.append(max(list_init))
    filter.append(min(list_end))

    for i in frequencies:
        if i >= filter[0] and i <= filter[1]:
            result.append(i)
    #print(filter)
    #print(result)
    #print(frequencies)
    #print(filterRanges)
    return len(result)

# Test with Sample Case 1
if __name__ == '__main__':
    # Sample Case 1
    if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    frequencies_count = int(input().strip())

    frequencies = []

    for _ in range(frequencies_count):
        frequencies_item = int(input().strip())
        frequencies.append(frequencies_item)

    filterRanges_rows = int(input().strip())
    filterRanges_columns = int(input().strip())

    filterRanges = []

    for _ in range(filterRanges_rows):
        filterRanges.append(list(map(int, input().rstrip().split())))

    result = countSignals(frequencies, filterRanges)

    fptr.write(str(result) + '\n')

    fptr.close()