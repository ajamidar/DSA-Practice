import math 
import os 
import random
import re
import sys


def findMinGeneration(layer):
    max_neurons = max(layer)
    diffs = [max_neurons - x for x in layer]
    total_ones = sum(d % 2 for d in diffs)
    total_twos = sum(d // 2 for d in diffs)
    generations = 0

    # Each generation, alternate between adding 1 and 2 neurons
    while total_ones > 0 or total_twos > 0:
        generations += 1
        if generations % 2 == 1:  # Odd generation: add 1 neuron
            if total_ones > 0:
                total_ones -= 1
            elif total_twos > 0:
                # Convert a '2' to a '1' if no '1's left
                total_twos -= 1
                total_ones += 1
        else:  # Even generation: add 2 neurons
            if total_twos > 0:
                total_twos -= 1
            elif total_ones > 1:
                # Convert two '1's to a '2' if no '2's left
                total_ones -= 2
                total_twos += 1
            elif total_ones == 1:
                # If only one '1' left, wait for next odd generation
                pass

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