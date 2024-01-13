def minSteps(self, s, t):
        sHash, tHash = {}, {}
        for i in range(len(s)):
            sHash[s[i]] = 1 + sHash.get(s[i], 0)
            tHash[t[i]] = 1 + tHash.get(t[i], 0)
        count = 0
        for i in sHash:
            if (sHash[i] - tHash.get(i, 0)) > 0:
                count += sHash[i] - tHash.get(i, 0)
        return count
