def longestCommonSubsequence(self, text1, text2):
     m, n = len(text1), len(text2)
     dp = [0] * (n + 1)

     for i in range(1, m + 1):
        diagonal = dp[0]

        for j in range(1, n + 1):
            temp = dp[j]
            if text1[i - 1] == text2[j - 1]:
                dp[j] = diagonal + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])

            diagonal = temp
     return dp[n]
