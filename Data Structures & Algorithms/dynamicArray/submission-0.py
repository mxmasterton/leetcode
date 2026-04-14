class DynamicArray:
    
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._data = [None] * self._capacity

    def get(self, i: int) -> int:
        return self._data[i]

    def set(self, i: int, n: int) -> None:
        self._data[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._data[self._size] = n
        self._size += 1 

    def popback(self) -> int:
        temp = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return temp

    def resize(self) -> None:
        self._data = self._data + [None] * self._capacity
        self._capacity *= 2

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity