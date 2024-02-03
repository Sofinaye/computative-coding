def maxSumAfterPartitioning(self, arr, k):  
    n = len(arr)
    sub = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, min(k, i) + 1):
            max_val = max(max_val, arr[i - j])
            sub[i] = max(sub[i], sub[i - j] + max_val * j)

    return sub[n]
