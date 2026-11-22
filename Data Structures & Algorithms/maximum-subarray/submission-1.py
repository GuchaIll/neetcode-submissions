class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        running = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            running = max(num, running + num)
            max_sum = max(max_sum, running)
        return max_sum 