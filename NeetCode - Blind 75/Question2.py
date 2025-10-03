class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

#a = Solution()
#print(a.isAnagram("anagram", "nagaram"))
    
#Time Complexity: O(n+m)
#Space Complexity: O(1)
#Where n is the length of string s and m is the length of string t