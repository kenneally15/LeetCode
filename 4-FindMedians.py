class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        med = (m+n+1)/2 - 1

        i = 0; j = 0

        while i+j <= med-1:
            if i >= m: j+=1
            elif j >= n: i+=1
            elif nums1[i] <= nums2[j]: i+=1
            else: j+=1
        

        #print(med,i,j)

        if i+1 < m:
            n12 = nums1[i+1]
        else:
            n12 = float('inf')

        n11 = nums1[i] if i<m else float('inf')
        n12 = nums1[i+1] if i+1<m else float('inf')
        n21 = nums2[j] if j<n else float('inf')
        n22 = nums2[j+1] if j+1<n else float('inf')

        numbers = [n11,n12,n21,n22]
        min1 = numbers[0]; min2 = numbers[1]
        
        for i in range(2, len(numbers)): 
            if numbers[i] < min1: 
                min2 = min1 
                min1 = numbers[i] 
            elif numbers[i] < min2: 
                min2 = numbers[i] 


        if int(2*med) % 2 == 0:
            median = min1
        else:
            median = (min1+min2)/2

        return median



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #Find the two smallest elements in list
        def findMinimums(numbers: List[int]):
            min1 = numbers[0]; min2 = numbers[1]
            for i in range(2, len(numbers)):
                if numbers[i] < min1:
                    min2 = min1
                    min1 = numbers[i]
                elif numbers[i] < min2:
                    min2 = numbers[i]
            return min1, min2
        
        #Initialize variables
        m = len(nums1)
        n = len(nums2)
        med = (m+n+1)/2 - 1
        i = 0; j = 0

        #Iterate to median
        while i+j <= med-1:
            if i >= m: j+=1
            elif j >= n: i+=1
            elif nums1[i] <= nums2[j]: i+=1
            else: j+=1

        #Find the correct indices
        n11 = nums1[i] if i<m else float('inf')
        n12 = nums1[i+1] if i+1<m else float('inf')
        n21 = nums2[j] if j<n else float('inf')
        n22 = nums2[j+1] if j+1<n else float('inf')
        numbers = [n11,n12,n21,n22]
        min1, min2 = findMinimums(numbers)

        #Even or Odd handling
        if int(2*med) % 2 == 0:
            median = min1
        else:
            median = (min1+min2)/2

        return median



                
                     
        