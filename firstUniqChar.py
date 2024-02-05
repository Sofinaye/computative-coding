def firstUniqChar(self, s):
      hashMap = {}
      for char in s:
          hashMap[char] = hashMap.get(char,0) + 1
      for j, char in enumerate(s):
          if hashMap[char] == 1:
              return j
      return -1
