class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for i in strs:
            ans += str(len(i))
            ans += '#'
            ans += i
        return ans 

    def decode(self, s: str) -> List[str]:
        ans = []
        i=0
        while i<len(s):
            t = s[i]
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            ans.append(word)
            i=j+1+length
        return ans 
            
