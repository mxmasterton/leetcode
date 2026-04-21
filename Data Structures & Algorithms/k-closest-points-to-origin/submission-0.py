class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[math.sqrt(x**2 + y**2), [x,y]] for (x,y) in points]
        heapq.heapify(points)

        out = []
        for _1 in range(k):
            _2, point = heapq.heappop(points)
            out.append(point)

        return out