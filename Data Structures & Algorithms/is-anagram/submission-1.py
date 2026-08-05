class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # approach - 02
        d1 , d2 = {} , {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]]=1
            else:
                d1[s[i]]+=1
            if t[i] not in d2:
                d2[t[i]]=1
            else:
                d2[t[i]]+=1
        return d1==d2
        # approach - 01
        # word1 = ''.join(sorted(s))
        # word2 = ''.join(sorted(t))
        # if word1==word2:
        #     return True 
        # return False