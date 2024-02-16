def findLeastNumOfUniqueInts(self, arr, k):
      freq = sorted(Counter(arr).values())
      for i, count in enumerate(freq):
          k -= count
          if k < 0:
              return len(freq) - i
      return 0
