class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = ''.join(sorted(s))
        word2 = ''.join(sorted(t))
        if word1==word2:
            return True 
        return False