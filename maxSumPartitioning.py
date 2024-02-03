def maxSumAfterPartitioning(self, arr, k):  
      arr.sort()
      count = k
      sub = []
      temp = arr.pop()
      for i in range(len(arr)+1):
            if count > 0:
                sub.append(temp)
                count -= 1
            else:
                temp = arr.pop()
                sub.append(temp)
                count = k -1
        return sum(sub)
      
