class MinHeap:
    def __init__(self):
        self._heap = [None]

    def _bubble_up(self, index):
        while index > 1 and self._heap[index] < self._heap[index // 2]:
            self._heap[index], self._heap[index // 2] = self._heap[index // 2], self._heap[index]
            index = index // 2

    def _bubble_down(self, index):
        while True:
            left = 2 * index
            right = 2 * index + 1
            smallest = index

            if right < len(self._heap) and self._heap[right] < self._heap[smallest]:
                smallest = right
            if left < len(self._heap) and self._heap[left] < self._heap[smallest]:
                smallest = left
            if smallest == index:
                break

            self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
            index = smallest
            

    def push(self, value: int) -> None:
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def pop(self) -> int:
        if len(self._heap) == 1:
            return -1
        if len(self._heap) == 2:
            return self._heap.pop()
        else:
            out = self._heap[1]
            self._heap[1] = self._heap.pop()
            self._bubble_down(1)
            return out

    def top(self) -> int:
        if len(self._heap) == 1:
            return -1
        else:
            return self._heap[1]

    def heapify(self, nums: List[int]) -> None:
        self._heap = [None] + nums
        for i in reversed(range(1, len(self._heap) // 2 + 1)):
            self._bubble_down(i)