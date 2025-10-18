class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

a = Solution()
print(a.topKFrequent([1,2,2,3,3,3], 2))

#Bucket sort solution.
#Time complexity: O(n)
#Space complexity: O(n)