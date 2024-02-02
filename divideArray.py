def divideArray(self, nums, k):
    result = []
    temp = []
    value = sorted(nums)
    for num in value:
        temp.append(num)
        if (len(temp)) == 3:
            if (max(temp)-min(temp) > k):
                return []
            else:
                result.append(temp)
                temp = []
    return result
