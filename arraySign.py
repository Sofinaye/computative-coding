def arraySign(self, nums):
      product = 1
      for num in nums:
          product *= num
          
      if product > 0:
          return 1
      elif product < 0:
          return -1
      else:
          return 0
