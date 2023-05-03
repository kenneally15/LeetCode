class Solution:
    def romanToInt(self, s: str) -> int:
        
        numeral = {
            "M": 1000,
            "CM": 900,
            "D":  500,
            "CD": 400,
            "C":  100,
            "XC":  90,
            "L":   50,
            "XL":  40,
            "X":   10,
            "IX":   9,
            "V":    5,
            "IV":   4,
            "I":    1
        }
        
        output = 0
        i = 0
        
        while i < len(s):
            
            if numeral.get(s[i:i+2]) != None:
                output += numeral[s[i:i+2]]
                i += 2
            elif numeral.get(s[i]) != None:
                output += numeral[s[i]]
                i += 1
        
        return output
                
            
            
        