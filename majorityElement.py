def majorityElement(self, nums):
      hashMap = {}
      for i in nums:
          hashMap[i] = hashMap.get(i,0) + 1
      for j in hashMap:
          if hashMap[j] > len(nums)/2:
              return j
