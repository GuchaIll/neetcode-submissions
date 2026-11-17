class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_count = max(piles)
        min_count = 1
    
        def simulate(k):
            needs = 0
            for pile in piles:
                needs += math.ceil(pile/k)
            return needs
        
        while min_count < max_count:
            mid = (min_count + max_count) // 2

            needs = simulate(mid)
            if needs <= h:
                max_count = mid
            else:
                #needs > h 
                min_count = mid+1

        return min_count