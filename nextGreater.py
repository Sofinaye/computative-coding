def nextGreaterElement(self, nums1, nums2):
      stack = []
      next = {}

      for num in nums2:
          while stack and num > stack[-1]:
              next[stack.pop()] = num
          stack.append(num)

      result = []
      for num in nums1:
          result.append(next.get(num, -1))

      return result
