def twoSum(self, numbers, target):
        hashMap = {}
        for i, num in enumerate(numbers, start = 1):
            if (target - num) in hashMap:
                return [hashMap[target - num], i]
            hashMap[num] = i
