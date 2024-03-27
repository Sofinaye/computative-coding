def numSubarrayProductLessThanK(self, nums, k):
      result = []
      if k <= 1: 
          return 0
      
      count = 0
      prd = 1  
      left = 0   
      
      for right, num in enumerate(nums):
          prd *= num  
          while prd >= k:  
              prd /= nums[left]
              left += 1
          count += right - left + 1  
      
      return count
