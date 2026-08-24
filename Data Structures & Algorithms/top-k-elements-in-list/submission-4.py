class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        # print(d)
        f = [[] for _ in range(len(nums)+1)]
        
        for i in d:
            f[d[i]].append(i)
        # print(f)
        ans = []
        for i in range(len(f)-1,-1,-1):
            for t in f[i]:
                ans.append(t)
            if len(ans)==k:
                break
        return ans 