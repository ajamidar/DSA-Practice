import math
import os
import random
import re
import sys

def getOptimalTeamSize(lowerSkill, higherSkill):
    n = len(lowerSkill)
    
    # Check if a team of size 'team_size' can be formed
    def can_form_team(team_size):
        # Create a list of (skill_level, lowerSkill, higherSkill) tuples
        developers = [(i+1, lowerSkill[i], higherSkill[i]) for i in range(n)]
        
        # Sort developers by their lowerSkill in descending order
        # This helps us prioritize developers who can tolerate fewer developers with lower skill
        developers.sort(key=lambda x: x[1], reverse=True)
        
        # Select the first 'team_size' developers
        selected = []
        for i in range(min(team_size, n)):
            selected.append(developers[i][0])
        
        # Sort selected developers by skill level
        selected.sort()
        
        # Check if all selected developers are satisfied
        for i in range(team_size):
            skill_level = selected[i]
            dev_index = skill_level - 1  # Convert skill level to 0-based index
            
            # Count developers with lower and higher skills in the selected team
            lower_count = i
            higher_count = team_size - i - 1
            
            # Check if constraints are satisfied
            if lower_count > lowerSkill[dev_index] or higher_count > higherSkill[dev_index]:
                return False
        
        return True
    
    # Binary search to find the maximum valid team size
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