def maxDepth(self, s):
      Max = 0
      current = 0

      for char in s:
          if char == '(':
              current += 1
              Max = max(Max, current)
          elif char == ')':
              current -= 1

      return Max
