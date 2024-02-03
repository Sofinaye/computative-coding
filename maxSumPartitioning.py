def maxSumAfterPartitioning(self, arr, k):  
      arr.sort()
      count = k
      sub = []
      temp = arr.pop()
      
