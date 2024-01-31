def dailyTemperatures(self, temperatures):
    days = 0
    result = []
    for i, temp in enumerate(temperatures):
        if i == len(temperatures) - 1:
            days = 0
            result.append(days)
            break
        for j in range(i+1, len(temperatures)):
            if temperatures[j] - temp > 0:
                days = j - i
                break
            else:
                days = 0
        result.append(days)
    return result
