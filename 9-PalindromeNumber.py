class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        s = str(x)

        #Check if negative
        if len(s) > 0 and s[0] == '-':
            return False
        
        #Calculate median
        m = len(s) // 2
        
        #Odd / Even pointers
        if len(s) % 2 == 1: 
            l,r = m-1,m+1
        else:
            l,r = m-1,m
        
        #Compare left and right
        while 0 <= l and r < len(s):
            if s[l] != s[r]:
                return False  
            l-=1; r+=1

        return True



