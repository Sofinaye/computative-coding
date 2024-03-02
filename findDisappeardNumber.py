def findDisappearedNumbers(self, nums):
      arr = []
      hashMap = set()
      for i in nums:
          if i not in hashMap:
              hashMap.add(i)
      for j in range(1, len(nums) + 1):
          if j not in hashMap:
              arr.append(j)
      return arr
