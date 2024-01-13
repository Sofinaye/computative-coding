def halvesAreAlike(self, s):
      half = len(s)/2
      a, b = 0, 0
      for i in range(half):
          if s[i] in {"a","e","i","o","u","A","E","I","O","U"}:
              a += 1
      for j in range(half, len(s)):
          if s[j] in {"a","e","i","o","u","A","E","I","O","U"}:
              b += 1
      if a == b:
          return True
      else:
          return False
