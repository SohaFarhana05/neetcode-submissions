class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                st.append(s[i])
            elif s[i]=='}' or s[i]==')' or s[i]==']':
                if len(st)==0:
                    return False
                here = st.pop()
                if s[i]=='}' and here!='{':
                    return False
                if s[i]==']' and here!='[':
                    return False
                if s[i]==')' and here!='(':
                    return False
                else:
                    continue
        if len(st)==0:
            return True
        return False