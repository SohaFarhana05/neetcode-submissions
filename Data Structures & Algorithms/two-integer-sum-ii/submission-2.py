class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            l , r = i+1, len(nums)-1
            t = target - nums[i]
            while l<=r:
                mid = l+(r-l)//2
                if nums[mid]==t:
                    return [i+1,mid+1]
                elif nums[mid]<t:
                    l=mid+1
                else:
                    r = mid - 1
        return []

