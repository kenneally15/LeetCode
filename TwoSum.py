class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i,j]

class Solution:
    def twoSum(self, nums: List[int], target: int):
        
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashMap and i != hashMap[complement]:
                return [i,hashMap[complement]]
        
        return [-1,-1]

class Solution:
    def twoSum(self, nums: List[int], target: int):
        
        hashMap = {}

        for i in range(len(nums)):
            
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            
            hashMap[nums[i]] = i
            
        return [-1,-1]


