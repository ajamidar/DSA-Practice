#!/bin/python3

import math
import os
import random
import re
import sys
import json



#
# Complete the 'getJSONDiff' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING json1
#  2. STRING json2
#

def getJSONDiff(json1, json2):
    # Write your code here
    obj1 = json.loads(json1)
    obj2 = json.loads(json2)
    
    common = set(obj1.keys()) & set(obj2.keys())
    diff = [k for k in common if obj1[k] != obj2[k]]
    
    return sorted(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    json1 = input()

    json2 = input()

    result = getJSONDiff(json1, json2)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
