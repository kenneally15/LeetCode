class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows in (0,1):
            return s

        output = ""
        modulus = 2*numRows - 2

        for row in range(numRows):
            
            sel1 = row
            sel2 = modulus-row

            for i in range(len(s)):
                if i % modulus in (sel1, sel2):
                    output += s[i]
        
        
        return output