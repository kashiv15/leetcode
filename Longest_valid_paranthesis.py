class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        l1=['(']
        l2=[')']
        b=0
        c=[]
        for i in range(len(s)):
            a=s[i]
            if a in l1:
                c.append(a)              
            elif a in l2:
                if len(c)>0 and l2.index(a)==l1.index(c[-1]):
                    c.pop()
                    b=b+2
        return b-2*len(c)
       """
        b=0
        c=[]
        c.append(-1)
        for i in range(len(s)):
            if s[i]=='(':
                c.append(i)
            else:
                c.pop()
                if len(c)==0:
                    c.append(i)
                else:
                    b=max(b,i-c[-1])
        return b
