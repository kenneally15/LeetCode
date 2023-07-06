class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)-len(needle)+1):

            j = 0   #offset
            while j < len(needle) and needle[j] == haystack[i+j]:
                j+=1
            
            if j == len(needle):
                return i
            
        return -1
            
            
            