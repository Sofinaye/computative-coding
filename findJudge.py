def findJudge(self, n, trust):
      trusts = [0] * (n + 1)
      for i, j in trust:
          trusts[i] -= 1  
          trusts[j] += 1  
      for k in range(1, n + 1):
          if trusts[k] == n - 1:
              return k  

      return -1
