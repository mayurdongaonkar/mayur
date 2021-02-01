s = "anagram"
t = "nagaram"

print(s[:-2])

class Solution():
    def isAnagram(self,s:str,t:str):
        return s == t[::-1]

s = Solution()
print(s.isAnagram(s,t))
        