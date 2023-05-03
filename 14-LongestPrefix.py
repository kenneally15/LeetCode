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

