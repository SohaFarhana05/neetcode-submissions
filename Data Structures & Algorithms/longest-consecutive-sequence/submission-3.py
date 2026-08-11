class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)
        maxi = 1
        here = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                here+=1
                maxi = max(maxi,here)
            else:
                here =1
        return maxi