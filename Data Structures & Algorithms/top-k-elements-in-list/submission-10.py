class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #tracking min_heap of max k elemnts
        min_heap = []
        frequencies = Counter(nums)

        for item, freq in frequencies.items():
            heapq.heappush(min_heap, (freq, item))
            
            while len(min_heap) > k:
                heapq.heappop(min_heap)

       
        return [item for freq, item in min_heap]

