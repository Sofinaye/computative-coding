 def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if indexDiff <= 0 or valueDiff < 0:
            return False

        bucket = {}

        def get_bucket_num(num, width):
            # Map a number to its bucket
            return (num - (-2**31)) // width

        for i, num in enumerate(nums):
            bucket_num = get_bucket_num(num, valueDiff + 1)

            if bucket_num in bucket:
                return True

            if bucket_num - 1 in bucket and abs(num - bucket[bucket_num - 1]) <= valueDiff:
                return True

            if bucket_num + 1 in bucket and abs(num - bucket[bucket_num + 1]) <= valueDiff:
                return True

            bucket[bucket_num] = num

            if i >= indexDiff:
                # Remove the leftmost element from the sliding window
                del bucket[get_bucket_num(nums[i - indexDiff], valueDiff + 1)]

        return False
