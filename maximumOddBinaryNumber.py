def maximumOddBinaryNumber(self, s):
      arr = []
      for i in s:
          if i == "1":
              if  i not in arr:
                  arr.append(i) 
              else:
                  arr.insert(0,i)
          else:
              arr.insert(-1, i)
      return "".join(arr)
