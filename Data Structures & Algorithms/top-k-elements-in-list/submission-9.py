class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #tracking min_heap of max k elemnts
        min_heap = []
        frequencies = Counter(nums)

        for item, freq in frequencies.items():
            if not min_heap or len(min_heap) < k:
                heapq.heappush(min_heap, (freq, item))
                continue
            
            if freq >= min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, item))

       
        res = []
        for freq, item in min_heap:
            res.append(item)
        return res

