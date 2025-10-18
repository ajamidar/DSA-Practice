from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

a = Solution()
print(a.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

#Time complexity: O(m*n)
#Space complexity: O(m*n) space for the output list.