class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        t = k
        l , r = 0 , 0
        d = {}
        maxi = 0
        ans = 0
        while r<len(s):
            if s[r] not in d:
                d[s[r]]=1
            else:
                d[s[r]]+=1
            maxi = max(maxi,d[s[r]])
            while (r-l+1) - maxi > k:
                d[s[l]]-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans
        # while r<len(s):
        #     if s[r] not in d:
        #         d[s[r]]=1
        #     else:
        #         d[s[r]]+=1
        #     while len(d)>2:
        #         d[s[l]]-=1
        #         l+=1
        #     maxi = max(maxi,r-l+1)
        #     r+=1
        return maxi