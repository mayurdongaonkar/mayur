words = ["practice", "makes", "perfect", "coding", "makes","practice"]

word1 = "practice" 
word2 = "coding"

print(words.index("practice"))

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        indx_1 = words.index(word1)
        indx_2 = words.index(word2)
        print(indx_1,indx_2)
        
        return abs(indx_1-indx_2)
    
s1 = Solution()
print(s1.shortestDistance(words,word1,word2))

    