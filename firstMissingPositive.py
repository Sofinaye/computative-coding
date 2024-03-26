def firstMissingPositive(self, nums):
      n = len(nums)
      hashSet = set(nums)
      for i in range(1, n+2):
          if i not in hashSet:
              return i
