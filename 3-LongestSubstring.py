class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        for i in range(len(s)): 
            charSeen = set()

            for j in range(i,len(s)):
                
                if s[j] in charSeen:
                    break
                else:
                    longest = max(longest,j-i+1)
                    charSeen.add(s[j])
        
        return longest
