class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l , r = 0 , len(nums) - 1
        while l<r:
            s = nums[l] + nums[r]
            if l<r and s>target:
                r-=1
            elif l<r and  s<target:
                l+=1
            elif s == target:
                return [l+1,r+1]