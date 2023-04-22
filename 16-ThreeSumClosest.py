class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        bestSum = inf
        nums.sort()

        print(nums)
        for i in range(len(nums)-2):

            j = i+1; k = len(nums)-1

            while j < k:

                checkSum = nums[i] + nums[j] + nums[k]
                
                if abs(target-checkSum) < abs(target-bestSum):
                    bestSum = checkSum


                if checkSum < target:
                    j+=1
                elif checkSum > target:
                    k-=1
                else:
                    break
        
        return bestSum


                
