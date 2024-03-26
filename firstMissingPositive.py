def firstMissingPositive(self, nums): 
      hashSet = set(nums)
      for i in range(1, len(nums)+2):
          if i not in hashSet:
              return i
