def getCommon(self, nums1, nums2):
      result = set(nums1)
      for i in  nums2:
          if i in result:
              return i
      return -1
