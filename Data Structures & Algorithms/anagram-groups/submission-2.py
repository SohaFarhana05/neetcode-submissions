class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        for i in strs:
            c = [0]*26
            for t in i:
                c[ord(t)-ord("a")]+=1
            res[tuple(c)].append(i)
        return list(res.values())