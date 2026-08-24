class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d = dict(sorted(d.items(),key=lambda x:x[1], reverse=True))
        ans = []
        for i in d:
            if k>0:
                ans.append(i)
                k-=1
            else:
                break

        return ans