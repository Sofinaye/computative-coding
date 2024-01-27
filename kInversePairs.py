def kInversePairs(self, n, k):
      arr = [[0] * (k + 1) for _ in range(n + 1)]
      arr[0][0] = 1  
      for i in range(1, n + 1):
          for j in range(k + 1):
              arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
              if j >= i:
                  arr[i][j] -= arr[i - 1][j - i]
              arr[i][j] = (arr[i][j] + (10**9 + 7)) % (10**9 + 7)

      return arr[n][k]
