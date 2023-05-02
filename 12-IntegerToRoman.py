class Solution:
    def intToRoman(self, num: int) -> str:
        
        numerals = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M", 5000:"Y"}
        output = ""

        while num > 0:

            n = len(str(num))
            base = 10**(n-1)

            digit = num // base

            if digit >= 5:

                if digit == 9:
                    output += numerals[base] + numerals[10*base]
                else:
                    output += numerals[5*base]
                    rem = digit % 5

                    while rem > 0:
                        output+= numerals[base]
                        rem-=1
            else:
                if digit == 4:
                    output += numerals[base] + numerals[5*base]
                else:
                    rem = digit

                    while rem > 0:
                        output += numerals[base]
                        rem-=1

            num = num % base

        return output     