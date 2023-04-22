class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = set()
        nums.sort()

        for i in range(len(nums)-2):
            
            j = i+1; k = len(nums)-1
            while j < k:

              sum = nums[i] + nums[j] + nums[k]

              if sum > 0:
                k-=1
              elif sum < 0:
                j+=1
              else:
                triplets.add((nums[i], nums[j], nums[k]))
                j+=1; k-=1
                    
        return triplets