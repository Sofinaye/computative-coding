def pivotIndex(self, nums):
      total = sum(nums)
      temp_left = 0
      for i in range(len(nums)):
          temp_right = total - nums[i] - temp_left
          if temp_left == temp_right:
              return i
          temp_left += nums[i]
      return -1
