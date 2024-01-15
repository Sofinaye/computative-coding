def longestConsecutive(self, nums):
    if len(nums) == 0:
        return 0
    strike = 1
    maxi = 1
    sort = sorted(nums)
    for i in range(len(sort)-1):
        if (sort[i] + 1 == sort[i+1]):
            strike += 1
            if strike > maxi:
                maxi = strike
        elif (sort[i]  == sort[i+1]):
            continue
        else:
            strike = 1
    return maxi
