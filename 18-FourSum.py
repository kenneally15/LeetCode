class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            
            pairs = set()

            i, j = 0, len(nums)-1
            while i < j:
                sum = nums[i] + nums[j]

                if sum < target: i+=1
                elif sum > target: j-=1
                else: pairs.add((nums[i],nums[j])); i+=1; j-=1
            
            return pairs
        
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            
            res = set()

            if not nums: return res

            #Base Case:
            if k == 2:
                return twoSum(nums,target)
            
            #Recursive Case:
            for i in range(len(nums)):
                for subset in kSum(nums[i+1:], target-nums[i], k-1):
                    res.add((nums[i],)+subset)
            
            return res


        nums.sort()
        return kSum(nums, target, 4)