class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, pre = [] , [1]
        suc = [1] * len(nums)
        for i in range(len(nums)-1):
            h = pre[-1]*nums[i]
            pre.append(h)
        for i in range(len(nums)-2,-1,-1):    
            suc[i] = suc[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans.append(pre[i]*suc[i])
        return ans 