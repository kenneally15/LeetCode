class Solution:
    def myAtoi(self, s: str) -> int:
        
        num = 0
        i = 0

        while i < len(s) and s[i] == ' ':
            i+=1
        
        pos = True if (i<len(s) and s[i]=='+') else False
        neg = True if (i<len(s) and s[i]=='-') else False

        if pos or neg:
            i+=1
        
        while i < len(s) and ('0' <= s[i] <= '9'):
            num = 10*num + int(s[i])
            i+=1
        
        if neg: num*=(-1)

        if num > 2**31-1: num = 2**31-1
        if num < -2**31: num = -2**31

        return num


        

        

        
    
        


        
        
        