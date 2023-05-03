class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""

        string = strs[0]
        for i in range(len(string)):
            for s in strs:
                if i>=len(s) or s[i] != string[i]:
                    return prefix
            
            prefix += string[i]
        
        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #Base Cases
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        #Find Prefix
        prefix = ""
        if len(strs) == 2:
            for i in range(min(len(strs[0]),len(strs[1]))):
                if strs[0][i] != strs[1][i]:
                    return prefix
                prefix += strs[0][i]
            return prefix
        
        #Recursion
        mid = len(strs) // 2
        left = self.longestCommonPrefix(strs[:mid])
        right = self.longestCommonPrefix(strs[mid:])
        
        return self.longestCommonPrefix([left,right])



            