import math
import os
import random
import re
import sys

def getOptimalTeamSize(lowerSkill, higherSkill):
    n = len(lowerSkill)
    
    # Check if a team of size k can exist
    def can_form_team(k):
        # For each developer, check if they can be part of a team of size k
        valid_devs = []
        
        for i in range(n):
            # For a developer to be in a team of size k:
            # - They can have at most lowerSkill[i] developers with lower skill level
            # - They can have at most higherSkill[i] developers with higher skill level
            
            # For a team of size k, a developer might be anywhere from position 0 to position k-1
            # At position j, there are j developers with lower skill and (k-j-1) with higher skill
            
            can_participate = False
            for j in range(k):
                lower = j
                higher = k - j - 1
                
                if lower <= lowerSkill[i] and higher <= higherSkill[i]:
                    can_participate = True
                    break
            
            if can_participate:
                valid_devs.append(i)
        
        # We need at least k valid developers
        return len(valid_devs) >= k
    
    # Binary search for the maximum valid team size
    left, right = 0, n
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_form_team(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lowerSkill_count = int(input().strip())

    lowerSkill = []

    for _ in range(lowerSkill_count):
        lowerSkill_item = int(input().strip())
        lowerSkill.append(lowerSkill_item)

    higherSkill_count = int(input().strip())

    higherSkill = []

    for _ in range(higherSkill_count):
        higherSkill_item = int(input().strip())
        higherSkill.append(higherSkill_item)

    result = getOptimalTeamSize(lowerSkill, higherSkill)

    fptr.write(str(result) + '\n')

    fptr.close()