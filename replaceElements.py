def replaceElements(self, arr):
      n = len(arr)
      right = -1

      for i in range(n - 1, -1, -1):
          current = arr[i]
          arr[i] = right
          right = max(right, current)

      return arr
