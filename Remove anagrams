def removeAnagrams(self, words):
        i = 1
        while i < len(words):
            if sorted(words[i - 1]) == sorted(words[i]):
                del words[i]
            else:
                i += 1
        return words
