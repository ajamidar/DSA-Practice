class Solution:
    def hasDuplicate(self, nums):
        return (len(set(nums)) < len(nums))

#Time Complexity: O(n)
#Space Complexity: O(n)