class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # currently i am returning the freq value 
        # instead of the actual number, but we need to sort 
        # according to the values
        values = [(-y, x) for x, y in freq.items()]
        heapq.heapify(values)
        for _ in range(k):
            res.append(heapq.heappop(values)[1])
        
        return res
