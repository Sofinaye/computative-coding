def rearrangeArray(self, nums):
        n = []
        p = []
        for i in nums:
            if i < 0:
                n.append(i)
            else:
                p.append(i)
        i = j = k = 0
        while i < len(n) and j < len(p):
            if k % 2 == 0:
                nums[k] = p[j]
                j += 1
            else:
                nums[k] = n[i]
                i += 1
            k += 1
        while i < len(n):
            nums[k] = n[i]
            i += 1
            k += 1
        while j < len(p):
            nums[k] = p[j]
            j += 1
            k += 1
        return nums
