class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data = []

        for i in range(len(points)):
            x, y = points[i]
            distance = -math.sqrt((x)**2 + (y)**2)
            if len(data) < k:
                heapq.heappush(data, (distance, i))
            elif len(data) == k:
                # negative distances
                if data[0][0] < distance:
                    heapq.heappushpop(data, (distance, i))
        
        return [points[index] for d, index in data]