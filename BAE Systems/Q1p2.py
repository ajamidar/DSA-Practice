import math 
import os 
import random
import re
import sys

def findMinGeneration(layer):
    target = max(layer)
    
    # Sort differences in descending order for greedy approach
    diffs = sorted([target - x for x in layer], reverse=True)
    
    generations = 0
    
    # Process each layer one by one
    while any(diff > 0 for diff in diffs):
        generations += 1
        
        # Find the layer with the largest remaining difference
        idx = 0  # Index of layer with max difference
        
        if generations % 2 == 1:  # Odd generation: add 1 neuron
            # Find first layer with non-zero difference
            while idx < len(diffs) and diffs[idx] == 0:
                idx += 1
                
            if idx < len(diffs):
                diffs[idx] -= 1
                
        else:  # Even generation: add 2 neurons
            # Find first layer with difference ≥ 2
            while idx < len(diffs) and diffs[idx] < 2:
                idx += 1
                
            if idx < len(diffs):
                diffs[idx] -= 2
            else:
                # If no layer needs 2+ neurons, find one that needs 1
                idx = 0
                while idx < len(diffs) and diffs[idx] == 0:
                    idx += 1
                    
                if idx < len(diffs):
                    diffs[idx] -= 1
        
        # Re-sort the differences after each generation
        diffs.sort(reverse=True)
    
    return generations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    layer_count = int(input().strip())

    layer = []

    for _ in range(layer_count):
        layer_item = int(input().strip())
        layer.append(layer_item)

    result = findMinGeneration(layer)

    fptr.write(str(result) + '\n')

    fptr.close()