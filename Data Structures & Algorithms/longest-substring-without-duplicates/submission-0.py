class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l , r = 0 , 0
        maxi = 0 
        # if s[l] not in d:
        #     d[s[l]]=1
        while r<len(s):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]]+=1
            while d[s[r]]>1:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            maxi = max(maxi,r-l+1)
            r+=1
        return maxi
