def uniqueOccurrences(self, arr):
      collection = {}
      hashSet = set()
      for i in arr:
          collection[i] = collection.get(i, 0) + 1
      for j in collection.values():
          if j in hashSet:
              return False
          hashSet.add(j)
      return True
