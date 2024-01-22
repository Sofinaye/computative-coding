def findErrorNums(self, nums):
    hashMap = set()
    missing = 0
    duplicate = 0
    num = sorted(nums)
    for l in (num):
        if l in hashMap:
            duplicate = l
        hashMap.add(l)
    for j in range(1, len(num)+1):
        if j not in hashMap:
            missing = j
            break
    return[duplicate, missing]
