class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        neg = 0

        #Check Negative
        if x<0:
            neg = 1
            x *= (-1)

        #Reverse digits
        while x > 0:
            
            #Pop
            pop = x % 10
            x //= 10

            #Push
            if rev > (2**31-1)/10 or (rev == (2**31-1)/10 and pop > 7): return 0
            if rev < (-2**31)/10 or (rev == (-2**31)/10 and pop < -8): return 0
            
            rev = rev * 10 + pop
        

        #Return negative
        if neg == 1:
            return (-1)*rev
        return rev


class Solution:
    def reverse(self, x: int) -> int:
        
        X = str(x); 
        Y = ""
        
        #Check negative
        if X[0] == "-":
            Y += "-"
            X = X[1:]

        #Reverse digits
        for i in range(len(X)):
            Y += X[len(X)-i-1]

        #Check bounds
        if -2**(31) <= int(Y) <= 2**(31) - 1:
            return int(Y)
        
        return 0


        
        
        
        
        
        