def containsNearbyDuplicate(self, nums, k):
        numCollection = {}
        for i, num in enumerate(nums):
            if num in numCollection and (i - numCollection[num] <= k):
                return True
            numCollection[num] = i
        
        return False
