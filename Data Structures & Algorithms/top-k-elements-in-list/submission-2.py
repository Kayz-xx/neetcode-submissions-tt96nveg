class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        values = []
        for num in freq.keys():
            heapq.heappush(values, (freq[num], num))
            if len(values) > k:
                heapq.heappop(values)

        for _ in range(k):
            res.append(heapq.heappop(values)[1])
        
        return res
