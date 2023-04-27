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


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x%10 == 0 and x != 0): 
            return False

        reverse = 0
        while x > reverse:
            reverse = reverse*10 + x%10
            x //= 10

        print(x, reverse)
        return (x == reverse or x == reverse//10)
            

