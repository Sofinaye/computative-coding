def productExceptSelf(self, nums):
        arr = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            arr[i] = left
            left *= nums[i]
        right = 1
        for j in range(len(nums) - 1, -1, -1):
            arr[j] *= right
            right *= nums[j]
        return arr
