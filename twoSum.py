def twoSum(self, nums, target):
      hashMap = {}
      for i, num in enumerate(nums, start=0):
          if (target - num) in hashMap:
              return [hashMap[target - num], i]
          hashMap[num] = i
