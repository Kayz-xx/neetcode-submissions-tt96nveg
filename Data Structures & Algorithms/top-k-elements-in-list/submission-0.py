class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        collection = []
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        sorted_list = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            collection.append(sorted_list[i][0])
        
        return collection
