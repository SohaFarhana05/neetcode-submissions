class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d = dict(sorted(d.items(),key=lambda x: x[1],reverse=True))
        t = []
        for i in d:
            if k>0:
                t.append(i)
                k-=1
            else:
                break
        return t