class MinHeap:
    def __init__(self):
        self.heap = [None]

    def _bubble_up(self, index: int) -> None:
        parent = index // 2
        while index > 1 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2

    def _bubble_down(self, index: int) -> None:
        child = 2 * index
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child += 1

            if self.heap[child] >= self.heap[index]:
                break

            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = 2 * index

    def push(self, val: int) -> None:
        """Pushes a value onto the heap."""
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        """Pops the smallest value off the heap."""
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return root

    def top(self) -> int:
        """Return the smallest value without popping it."""
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return -1
        
    def heapify(self, nums: List[int]) -> None:
        """Transforms a list into a heap in-place"""
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._bubble_down(i)