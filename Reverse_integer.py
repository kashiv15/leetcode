class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def xrev(x):
                b=0
                while(x>0):
                    a=x%10
                    b=b*10+a
                    x=x//10
                return b
        
        if(x<0):
            x=x*-1
            k=xrev(x)
            if (abs(k)>2**31-1):
                return 0
            else:
                return k*-1
        if(x>0):
            b=xrev(x)
            if(abs(b)>2**31-1):
                return 0
            else:
                return b
        if(x==0):
            return 0
        
