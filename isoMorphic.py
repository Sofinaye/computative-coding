def isIsomorphic(self, s, t):
      d1, d2 = {}, {}
      for i, j in zip(s, t):
          
          if ((i in d1 and d1[i] != j) or (j  in d2 and d2[j] != i)):
              return False
          d1[i], d2[j] = j , i 

      return True
