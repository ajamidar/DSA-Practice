class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
    
a = Solution()
print(a.twoSum([4,5,6], 10))

#Time complexity: O(n)
#Space complexity: O(n)
#Hash map solution.