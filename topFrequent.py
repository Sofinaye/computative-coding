def topKFrequent(self, nums, k):
        occurences = {}
        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1
        sorted_values = [i for i in sorted(occurences.items(), key=lambda x: x[1], reverse=True)]
        return [sorted_values[i][0] for i in range(k)]
