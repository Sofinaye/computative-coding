def findDuplicates(self, nums):
       duplicates = []
       i = 0
       while i < len(nums):
           if nums[i] != nums[nums[i] - 1]:  
               nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  
           else:
               i += 1

       for i in range(len(nums)):
           if nums[i] != i + 1:
               duplicates.append(nums[i])

       return duplicates
