def lengthOfLastWord(self, s):
       s = s.strip()
       last_word = s[s.rfind(' ') + 1:]
       return len(last_word)
