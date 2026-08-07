class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            h = ''.join(sorted(i))
            if h not in d:
                d[h]=[i]
            else:
                d[h].append(i)
        ans = []
        for i in d:
            ans.append(d[i])
        return ans 
