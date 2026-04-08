class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data = []

        for i in range(len(points)):
            x, y = points[i]
            distance = -((x)**2 + (y)**2)
            if len(data) < k:
                heapq.heappush(data, (distance, i))
            else:
                # negative distances
                if distance > data[0][0]:
                    heapq.heappushpop(data, (distance, i))
        
        return [points[index] for d, index in data]