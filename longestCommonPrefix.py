def longestCommonPrefix(self, strs):
      strs.sort()
      first_str = strs[0]
      last_str = strs[-1]
      for i in range(len(first_str)):
          if i >= len(last_str) or first_str[i] != last_str[i]:
              return first_str[:i]
      return first_str
