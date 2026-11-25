class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        max_freq = 0
        running_sum = 0
        k_count = nums.count(k)

        for v in range(1, 51):
            if v == k:
                continue
            running_sum = 0

            for i in range(len(nums)):
                gain = 0
                if nums[i] == k:
                    gain = -1
                elif nums[i] == v:
                    gain = 1

                running_sum = max(0, running_sum + gain)
                max_freq = max(running_sum, max_freq)

        return k_count + max_freq
