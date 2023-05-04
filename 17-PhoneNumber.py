class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return []
        
        output = [""]
        for i in range(len(digits)):
            temp = []
            for c in dic[digits[i]]:
                for string in output:

                    newstring = string + c
                    temp.append(newstring)
                
            
            output = temp
        
        return output



class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        if len(digits) == 0:
            return ans

        self.dfs(digits, "", ans, dic)

        return ans


    def dfs(self, digits: str, prefix: str, ans: List[str], dic):

        #Base case
        if len(digits) == 0:
            ans.append(prefix)
            return
        
        #Recursive case
        chars = dic[digits[0]]
        for c in chars:
            self.dfs(digits[1:], prefix+c, ans, dic)
        
    