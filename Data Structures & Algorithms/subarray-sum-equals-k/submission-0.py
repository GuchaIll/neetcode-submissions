class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       #prefix sum:
       #nums[1:K+1] - nums[1:k] = nums[k:k+1]

       #
        freq = defaultdict(int)
        count = 0

        curr = nums[0]

        freq[0] += 1
        freq[curr] += 1

        if nums[0] == k:
                count += 1
        for i in range(1,len(nums)):
            curr += nums[i]
            #prefix[i] - prefix[l] = k
            #prefix[l] = prefix[i] - k

            start = curr - k
            if start in freq:
                count += freq[start]

            freq[curr] += 1

        return count

    
