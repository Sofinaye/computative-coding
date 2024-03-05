def replaceElements(self, arr):
        temp_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(arr[i], temp_max)
            arr[i] = temp_max
            temp_max = new_max

        return arr
