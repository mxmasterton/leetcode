class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque() # [-count, idle_time]

        while max_heap or queue:
            time += 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time
