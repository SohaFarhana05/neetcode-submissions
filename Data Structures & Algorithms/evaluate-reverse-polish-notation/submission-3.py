class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for i in range(len(tokens)):
            # print(st)
            if tokens[i].lstrip('-').isdigit():
                st.append(int(tokens[i]))
            if tokens[i]=='+':
                a , b = st.pop() , st.pop()
                st.append(a+b)
                # print(st)
            if tokens[i]=='-':
                a , b = st.pop() , st.pop()
                st.append(b-a)
            if tokens[i]=='*':
                a , b = st.pop() , st.pop()
                st.append(a*b)
            if tokens[i]=='/':
                a , b = st.pop() , st.pop()
                st.append(int(b/a))
        return st.pop()