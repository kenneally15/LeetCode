class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ""

        #Odd Case
        for i in range(len(s)):

            left = right = i
            while left >= 0 and right < len(s):

                if s[left] != s[right]: 
                    break
            
                left-=1; right+=1

            if len(s[left+1:right]) > len(longest):
                longest = s[left+1:right]
        

        #Even Case
        for i in range(len(s)-1):

            left, right = i, i+1
            while left >= 0 and right < len(s):

                if s[left] != s[right]:
                    break
                
                left-=1; right+=1
            
            if len(s[left+1:right]) > len(longest):
                longest = s[left+1:right]
        
        return longest

        