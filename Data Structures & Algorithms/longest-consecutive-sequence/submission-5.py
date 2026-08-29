class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        t = 1
        if len(nums)<=1:
            return len(nums)
        maxi = 1
        for i in nums:
            if (i-1) not in s:

                while t+i in s:
                    t+=1
                    maxi = max(maxi,t)     
            t=1
        return maxi
