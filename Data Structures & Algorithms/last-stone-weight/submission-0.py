class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        print(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            diff = x - y
            if diff > 0:
                heapq.heappush(heap, -diff)

        if len(heap) == 1:
            return -heap[0]
        else:
            return 0