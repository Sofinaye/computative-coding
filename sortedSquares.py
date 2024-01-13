def sortedSquares(self, nums):
        arr = []
        for i in nums:
            arr.append(i**2)
        arr.sort()
        return arr
