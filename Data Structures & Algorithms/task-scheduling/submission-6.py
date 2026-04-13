class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        m = defaultdict(int)
        queue = []
        time = 0

        for task in tasks:
            m[task] += 1
        
        for value in m.values():
            heapq.heappush_max(heap, value)

        while heap or queue:
            time += 1
            if heap:
                value = heapq.heappop_max(heap)
                value -= 1
                if value > 0:
                    queue.append((value, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush_max(heap, queue.pop(0)[0])

        return time